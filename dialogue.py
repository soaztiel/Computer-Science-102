import pygame
from pygame.sprite import Sprite, Group
import time

# configuration
HEART_THRESHOLDS = [3, 6, 9, 12, 15]  # hearts needed per stage (1..5)
HEART_PICKUP_SOUND = None  # set to a pygame.mixer.Sound if desired
DIALOGUE_ADVANCE_KEY = pygame.K_SPACE

# Map interest keys to display names and colors for heart sprites (colors for developer use)
LOVE_INTERESTS = {
    "li1": {"name": "Love Interest #1", "color": (255, 120, 140)},
    "li2": {"name": "Love Interest #2", "color": (120, 180, 255)},
    "li3": {"name": "Love Interest #3", "color": (255, 160, 220)},
}

# dialogue box itself
class DialogueBox:
    """Simple textbox UI that overlays game. Press SPACE to advance.
    Supports speaker prefix like 'Name: Dialogue' for small label display.
    Can accept callback when sequence completes.
    """

    def __init__(self, screen, font=None, height=120, alpha=200):
        self.screen = screen
        self.active = False
        self.dialogue = []
        self.index = 0
        self.on_complete = None
        self.freeze_game = False

        # font
        self.font = font if font else pygame.font.Font(None, 26)
        self.label_font = pygame.font.Font(None, 20)

        # box geometry
        w = screen.get_width()
        h = height
        self.box_rect = pygame.Rect(40, screen.get_height() - h - 20, w - 80, h)
        self.surface = pygame.Surface((self.box_rect.w, self.box_rect.h))
        self.surface.set_alpha(alpha)
        self.surface.fill((20, 20, 20))

        # internal wrap settings
        self.line_height = self.font.get_linesize()
        self.padding = 12

    def start(self, dialogue_list, on_complete=None, freeze_game=True):
        """Start a dialogue sequence. dialogue_list: list of strings (may include 'Name: text')."""
        if not dialogue_list:
            return
        self.dialogue = dialogue_list
        self.index = 0
        self.active = True
        self.on_complete = on_complete
        self.freeze_game = freeze_game

    def stop(self):
        self.active = False
        if callable(self.on_complete):
            try:
                self.on_complete()
            except Exception:
                pass
        self.on_complete = None
        self.freeze_game = False

    def update(self, events):
        if not self.active:
            return

        for e in events:
            if e.type == pygame.KEYDOWN and e.key == DIALOGUE_ADVANCE_KEY:
                self.index += 1
                if self.index >= len(self.dialogue):
                    self.stop()

    def draw(self):
        if not self.active:
            return
        # draw background
        self.screen.blit(self.surface, (self.box_rect.x, self.box_rect.y))
        # parse speaker
        raw = self.dialogue[self.index]
        speaker = None
        text = raw
        if ":" in raw:
            # split only on first colon
            sp, rest = raw.split(":", 1)
            if sp.strip() != "":
                speaker = sp.strip()
                text = rest.strip()

        # speaker label
        if speaker:
            label_surf = self.label_font.render(speaker, True, (240, 200, 200))
            self.screen.blit(label_surf, (self.box_rect.x + self.padding, self.box_rect.y + 6))

        # draw wrapped text
        wrapped = self._wrap_text(text, self.font, self.box_rect.w - self.padding * 2)
        for i, line in enumerate(wrapped):
            y = self.box_rect.y + 30 + i * self.line_height
            surf = self.font.render(line, True, (235, 235, 235))
            self.screen.blit(surf, (self.box_rect.x + self.padding, y))

    def _wrap_text(self, text, font, max_width):
        words = text.split(" ")
        lines = []
        current = ""
        for word in words:
            test = current + (word + " ")
            if font.size(test)[0] <= max_width:
                current = test
            else:
                lines.append(current.strip())
                current = word + " "
        if current:
            lines.append(current.strip())
        return lines

# invisible relationship meter
class RelationshipManager:
    """Tracks hearts for each love interest. Invisible to player but always active.
    Fires callbacks when stage increments (1..5), which trigger dialogue."""

    def __init__(self, dialogue_manager=None):
        # hearts count per interest id (strings like 'li1')
        self.hearts = {k: 0 for k in LOVE_INTERESTS.keys()}
        self.stage = {k: 0 for k in LOVE_INTERESTS.keys()}  # 0..5
        self.dialogue_manager = dialogue_manager

    def add_heart(self, interest_id, amount=1):
        if interest_id not in self.hearts:
            return
        self.hearts[interest_id] += amount
        # clamp if excessive
        if self.hearts[interest_id] > HEART_THRESHOLDS[-1]:
            self.hearts[interest_id] = HEART_THRESHOLDS[-1]
        self._recalc_stage(interest_id)

    def _recalc_stage(self, interest_id):
        count = self.hearts[interest_id]
        new_stage = 0
        for i, t in enumerate(HEART_THRESHOLDS, start=1):
            if count >= t:
                new_stage = i
        if new_stage != self.stage[interest_id]:
            old = self.stage[interest_id]
            self.stage[interest_id] = new_stage
            # trigger dialogue pack for stage up
            if self.dialogue_manager:
                self.dialogue_manager.on_stage_increase(interest_id, old, new_stage)

    def get_stage(self, interest_id):
        return self.stage.get(interest_id, 0)

    def get_top_interest(self):
        # returns interest id with highest stage, tie-breaker highest hearts
        top = None
        for k in self.hearts.keys():
            if top is None:
                top = k
                continue
            if self.stage[k] > self.stage[top]:
                top = k
            elif self.stage[k] == self.stage[top] and self.hearts[k] > self.hearts[top]:
                top = k
        return top

# dialogue (packs, triggers, and unique options)
class DialogueManager:
    """Holds dialogue packs and starts DialogueBox sequences when triggered.
    Packs keyed by (interest_id, stage) and by general keys (e.g., 'chapter4_intro').
    """

    def __init__(self, screen):
        self.screen = screen
        self.dialogue_box = DialogueBox(screen)
        self.packs = {}
        self._register_default_packs()

    def start_pack(self, key, freeze_game=True, on_complete=None):
        """Start a pack. key can be tuple (interest_id, stage) or string."""
        pack = self.packs.get(key)
        if not pack:
            # no pack found, ignore
            return
        self.dialogue_box.start(pack, on_complete=on_complete, freeze_game=freeze_game)

    def update(self, events):
        self.dialogue_box.update(events)

    def draw(self):
        self.dialogue_box.draw()

    def on_stage_increase(self, interest_id, old_stage, new_stage):
        """Called by RelationshipManager when an interest stages up.
        We automatically trigger the corresponding pack if present.
        """
        # try tuple key first
        key = (interest_id, new_stage)
        if key in self.packs:
            self.start_pack(key, freeze_game=True)
            return
        # or named key
        named = f"{interest_id}_stage_{new_stage}"
        if named in self.packs:
            self.start_pack(named, freeze_game=True)

    def _register_default_packs(self):
        # Insert the sample dialogues from earlier into packs
        # Prologue / general:
        self.packs["prologue_opening"] = [
            "*A thunderous crack echoes. Doomguy emerges from a collapsing Hell portal.*",
            "Doomguy: ...this isn't Earth.",
            "??? : You’re not from around here, are you?",
            "Doomguy: (shakes head)",
            "??? : Follow me. This cave is crawling with demons—and something else."
        ]

        # Love Interest #1 meeting & stage-specific (li1 stage 1..5)
        self.packs[("li1", 1)] = [
            "Love Interest #1: Careful! These caverns twist on themselves.",
            "Love Interest #1: I'll guide you… if you help me survive.",
            "Doomguy: (nods resolutely)",
            "Love Interest #1: You're surprisingly gentle for someone who just punched a demon in half.",
            "Love Interest #1: ...I like that about you."
        ]
        # more intimate lines for higher stages
        self.packs[("li1", 2)] = [
            "Love Interest #1: That jump you pulled off—I've never seen anyone move like that.",
            "Love Interest #1: You're reckless, but... dependable.",
            "Doomguy: ...",
            "Love Interest #1: Stay close."
        ]
        self.packs[("li1", 3)] = [
            "Love Interest #1: I trust you with my life now.",
            "Love Interest #1: If you ever leave, I want you to promise me one thing—don't forget who waited.",
            "Doomguy: (quietly) I won't."
        ]
        self.packs[("li1", 4)] = [
            "Love Interest #1: We make a good team. Maybe too good.",
            "Love Interest #1: My heart's been... safer since you showed up.",
            "Doomguy: ..."
        ]
        self.packs[("li1", 5)] = [
            "Love Interest #1: I thought the worst of you when I first saw you.",
            "Love Interest #1: Turns out, I was wrong. You're my anchor.",
            "Doomguy: (soft) ..."
        ]

        # Love Interest #2: rescue stage packs
        self.packs[("li2", 1)] = [
            "Love Interest #2: *cough* You… you took down those things like they were nothing.",
            "Doomguy: ...",
            "Love Interest #2: Thank you. I would've rotted in that cage.",
            "Love Interest #2: Let me repay you. Let me fight with you."
        ]
        self.packs[("li2", 3)] = [
            "Love Interest #2: You trust me. That means more than you know.",
            "Love Interest #2: We'll get out of this together."
        ]
        self.packs[("li2", 5)] = [
            "Love Interest #2: When the world is quiet, I can hear you breathing.",
            "Love Interest #2: Stay with me."
        ]

        # Love Interest #3: berserk rescue
        self.packs[("li3", 1)] = [
            "Love Interest #3: I told them… I TOLD them I could handle this alone!",
            "*Berserk demons swarm. Doomguy tears through them.*",
            "Love Interest #3: You saved me. And now you're stuck with me.",
            "Love Interest #3: Try not to fall for me too fast, marine."
        ]
        self.packs[("li3", 4)] = [
            "Love Interest #3: If there wasn't a virus here, I'd think you just wanted to be near me.",
            "Love Interest #3: And maybe... you'd be right."
        ]
        self.packs[("li3", 5)] = [
            "Love Interest #3: I would follow you through every portal.",
            "Love Interest #3: Hell, I'd walk through your timeline with you."
        ]

        # Chapter 3 -> Chapter 4 transition & Chapter 4 dialogue packs
        self.packs["chapter3_to_4"] = [
            "Doomguy: It's too dangerous. Stay.",
            "Love Interest: No. Whatever's infecting these demons isn't stopping.",
            "Love Interest: You protected me. Let me protect you.",
            "Doomguy: ...Fine.",
            "*They step through the pink portal together.*"
        ]

        self.packs["chapter4_intro"] = [
            "*The realm pulses like a living organ.*",
            "Love Interest: This place… it's alive.",
            "Doomguy: Virus core.",
            "Love Interest: Then we end this. Together."
        ]

        self.packs["satan_reveal"] = [
            "Satan: Foolish mortal. You were meant to be my perfect vessel!",
            "Satan: Your rage, your will—irresistible!",
            "Doomguy: No.",
            "Satan: And those hearts you hoarded? Counteragents! You twisted my virus into… affection.",
            "Satan: Disgusting."
        ]

        self.packs["final_victory"] = [
            "Satan: IMPOSSIBLE—LOVE CANNOT—",
            "*Doomguy ends him.*",
            "Love Interest: …You did it.",
            "Doomguy: We did."
        ]

# cutscene / boss manager
class CutsceneScripter:
    """Simple cutscene script runner. A script is a list of actions:
        - {"type": "dialog", "pack_key": key}
        - {"type": "wait", "seconds": float}
        - {"type": "callback", "fn": callable}
    The scripter will start dialogues via DialogueManager and wait until they finish.
    """

    def __init__(self, dialogue_manager):
        self.dm = dialogue_manager
        self.queue = []
        self.active = False
        self._waiting_dialogue = False
        self._wait_until = 0

    def play_script(self, script, on_complete=None):
        self.queue = list(script)
        self.active = True
        self.on_complete = on_complete
        self._waiting_dialogue = False
        self._wait_until = 0
        # freeze gameplay while cutscene runs (the dialogue box also sets freeze)
        if self.dm:
            self.dm.dialogue_box.freeze_game = True

    def update(self, events, dt):
        if not self.active:
            return
        # update dialogue manager so box processes events
        self.dm.update(events)

        # waiting for a dialogue to finish
        if self._waiting_dialogue:
            if not self.dm.dialogue_box.active:
                self._waiting_dialogue = False
            else:
                return

        # waiting for time
        if time.time() < self._wait_until:
            return

        if not self.queue:
            self.active = False
            # unfreeze gameplay
            if self.dm:
                self.dm.dialogue_box.freeze_game = False
            if callable(self.on_complete):
                try:
                    self.on_complete()
                except Exception:
                    pass
            return

        action = self.queue.pop(0)
        t = action.get("type")
        if t == "dialog":
            pack_key = action.get("pack_key")
            self.dm.start_pack(pack_key, freeze_game=True)
            self._waiting_dialogue = True
        elif t == "wait":
            self._wait_until = time.time() + float(action.get("seconds", 0))
        elif t == "callback":
            fn = action.get("fn")
            if callable(fn):
                try:
                    fn()
                except Exception:
                    pass
        else:
            # unknown type: skip
            pass

class BossFightManager:
    """Manages boss fight states and coordinates cutscenes. Designed to integrate simply:
        - call start_boss() to initiate the fight sequence
        - call update(events, dt) and draw() to render dialogue/cutscenes.
        - expose freeze_game flag for main loop to pause other updates
    """

    def __init__(self, dialogue_manager, relationship_manager):
        self.dm = dialogue_manager
        self.rm = relationship_manager
        self.scripter = CutsceneScripter(self.dm)
        self.state = "idle"  # idle -> intro_cutscene -> phase1 -> phase2 -> defeated -> done
        self.freeze_game = False
        # boss internal HP
        self.phase1_hp = 200
        self.phase2_hp = 300
        self.on_defeat = None

    def start_boss(self, on_defeat=None):
        if self.state != "idle":
            return
        self.on_defeat = on_defeat
        self.state = "intro_cutscene"
        # play intro cutscene script (Satan's reveal)
        script = [
            {"type": "dialog", "pack_key": "chapter4_intro"},
            {"type": "dialog", "pack_key": "satan_reveal"},
        ]
        self.scripter.play_script(script, on_complete=self._enter_phase1)
        self.freeze_game = True

    def _enter_phase1(self):
        self.state = "phase1"
        self.freeze_game = False  # allow gameplay to resume for the player to fight
        # can optionally notify the game to spawn phase1 enemies
        # The game loop should poll/add boss_manager.state to adapt behavior.

    def damage_boss(self, amount):
        """Call this when player damages the boss. Manager handles stage transitions."""
        if self.state == "phase1":
            self.phase1_hp -= amount
            if self.phase1_hp <= 0:
                # transition to phase 2 cutscene
                self.state = "phase2_cutscene"
                self.freeze_game = True
                script = [
                    {"type": "dialog", "pack_key": "satan_reveal"},  # can reuse or create new
                    {"type": "wait", "seconds": 0.6},
                    {"type": "dialog", "pack_key": "final_victory"},
                ]
                self.scripter.play_script(script, on_complete=self._enter_phase2)
        elif self.state == "phase2":
            self.phase2_hp -= amount
            if self.phase2_hp <= 0:
                self.state = "defeated"
                self.freeze_game = True
                # final victory pack played, then finish
                self.scripter.play_script([{"type": "dialog", "pack_key": "final_victory"}], on_complete=self._on_defeat)

    def _enter_phase2(self):
        self.state = "phase2"
        self.freeze_game = False  # gameplay resumes, but now boss uses phase2 moves

    def _on_defeat(self):
        self.state = "done"
        self.freeze_game = False
        # depending on top relationship stage, you may want to call different endings
        top = self.rm.get_top_interest()
        stage = self.rm.get_stage(top) if top else 0
        # rudimentary end selection - game should call your own end logic
        if callable(self.on_defeat):
            try:
                self.on_defeat(top, stage)
            except Exception:
                pass

    def update(self, events, dt):
        self.scripter.update(events, dt)
        self.freeze_game = self.scripter.active or (self.state in ["intro_cutscene", "phase2_cutscene"])

    def draw(self):
        # only draws dialogue box via dialogue manager
        self.dm.draw()

# main container (simplifies integration)
class ValenDOOMManagers:
    """This is a container to hold and update all systems in one call from the main loop.
    So for example:
        managers = ValenDOOMManagers(screen)
        # in main loop:
        events = pygame.event.get()
        managers.update(events, dt)
        managers.draw()
        if managers.freeze_game: skip player/enemy updates
    """

    def __init__(self, screen):
        self.screen = screen
        self.dialogue_manager = DialogueManager(screen)
        self.relationship_manager = RelationshipManager(dialogue_manager=self.dialogue_manager)
        self.boss_manager = BossFightManager(self.dialogue_manager, self.relationship_manager)

        # convenience: sprite group for heart pickups
        self.heart_sprites = Group()

    @property
    def freeze_game(self):
        # freeze if any cutscene running or dialogue box says freeze
        return (self.dialogue_manager.dialogue_box.freeze_game
                or self.boss_manager.freeze_game
                or self.boss_manager.scripter.active)

    def update(self, events, dt):
        """Call once per frame. dt is seconds since last frame."""
        # update hearts
        self.heart_sprites.update(dt)
        # process dialogue manager event updates
        self.dialogue_manager.update(events)
        # update boss manager and cutscenes
        self.boss_manager.update(events, dt)

    def draw(self):
        # hearts under gameplay up to the game's draw order
        self.heart_sprites.draw(self.screen)
        # dialogue & boss UI draw last
        self.boss_manager.draw()
        self.dialogue_manager.draw()

    def pickup_check(self, player_rect):
        """Call from main loop after physics to detect heart pickups:
           For every heart collided, call its on_pickup to add to relationship manager.
        """
        collisions = [s for s in self.heart_sprites if s.rect.colliderect(player_rect)]
        for heart in collisions:
            heart.on_pickup(self.relationship_manager)