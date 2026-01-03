# hitTarget.py
#
# This is a game whose object is to hit a moving target
#   with a bomb fired from a cannon.
#
#   The player has NUMBOMBS bombs and loses the game when the bomb arsenal is
#   exhausted.  The bomb is fired from the cannon by pressing on the space bar.
#

import pygame
from random import randint

pygame.init()

WIDTH = 800
HEIGHT = 600

NUMBOMBS = 5
TARGETSIZE = 50
CANNON_DY = 10
BOMB_DX = 25
BACKGROUNDCOLOR = (200,255,200)
FONTCOLOR = (0,0,0)

screen = pygame.display.set_mode((WIDTH,HEIGHT))   # Construct the screen and
pygame.display.set_caption("Hit The Target")       # set its caption.


##############################################################################
# A Target sprite is the target the cannon shoots at.
class Target(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)    # Initialize the sprite.
        # Create a target Surface by loading an image
        self.image = pygame.image.load("target.gif")    
        self.image = self.image.convert()
        self.image.set_colorkey(self.image.get_at((1,1))) # Set the transparent color
        self.image = pygame.transform.scale(self.image, (TARGETSIZE,TARGETSIZE))
        self.rect = self.image.get_rect()
        # Initial location and speed of the target:
        self.rect.center = (screen.get_width()-100, screen.get_height()//2)
        self.dy = 5


    #  self.update() - Move the target up or down the screen.  When the target 
    #                  moves off the screen, a new random speed and vertical 
    #                  direction is chosen. 
    def update(self):

        # Move the target vertically, with a little random variation.
        self.rect.centery += (self.dy + randint(-2,10))

        # If the target moves off-screen, pick a new random speed and direction
        if self.rect.bottom <= 0 or self.rect.top >= screen.get_height():

            direction = randint(0,1)              # Flip a coin
            
            if direction == 0:                    # Downwards
                self.rect.bottom = 0              #   starting from the top
                self.dy = randint(5, 20)          #   with a random speed.
               
            else:                                 # Upwards
                self.rect.top=screen.get_height() #   starting from the bottom
                self.dy = randint(-20, -5)        #   with a random speed.


##############################################################################
# A Cannon sprite is used to shoot a bomb at a Target.
class Cannon(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)    # Initialize the sprite.
        self.image = pygame.image.load("cannon.gif")   #   Load image onto a Surface
        self.image = self.image.convert()              #   Convert pixel format.
        aColor = self.image.get_at((1,1))              #   Color to make transparent.
        self.image.set_colorkey(aColor)                #   Now make it transparent.
        self.image = pygame.transform.scale(self.image, (200,100))  # Scale surface.
        self.rect = self.image.get_rect();             # Get rectangle for the image.
        self.rect.center = (120, screen.get_height()//2)  # Initial cannon location.

    #  Instead of using update() we use two other functions:
    #                              self.moveup()
    #                              self.movedown()  
    
    #  self.moveup() - Move the cannon CANNON_DY pixels up, but stay on the screen.
    def moveup(self):
        if (self.rect.top > CANNON_DY):
            self.rect.centery -= CANNON_DY

    #  self.movedown() - Move the cannon CANNON_DY pixels down, but stay on the screen.
    def movedown(self):
        if (self.rect.bottom < (screen.get_height()-CANNON_DY) ):
            self.rect.bottom += CANNON_DY

    #  self.get_pos() - Returns the center of the cannon rectangle.  This is 
    #                     used to determine where to shoot the bomb from.  
    def get_pos(self):
        return self.rect.center

        
##############################################################################
# A Bomb sprite is fired by the cannon toward the target.
class Bomb(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)       # Initialize the sprite.

        # Create a bomb Surface by loading an image
        self.image = pygame.image.load("bomb.png")
        self.image = self.image.convert()
        self.image.set_colorkey(self.image.get_at((1,1)))
        self.image = pygame.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect()
        self.rect.center = (-100, -100)           # Move bomb offstage.
        self.dx = 0                               # Speed is 0 until fired.
        self.shooting = False        # Initially the bomb is not in flight.

    # self.fire() - Initiate the firing of a Bomb, but only if it is 
    #                 not already in flight.  The bomb is moved to the
    #                 location of the cannon's muzzle so that it is seen
    #                 to fire from the cannon.  Set its speed and keep
    #                 track of the fact that it is being shot.
    def fire(self, cannon_pos):
        if not self.shooting:
            self.rect.center = cannon_pos  # Move Bomb to cannon.
            self.rect.centery -= 33        # Adjust bomb position to
            self.rect.centerx += 88       #   the cannon's muzzle
            self.dx = BOMB_DX              # Set its velocity.
            self.shooting = True           # The Bomb is in flight
            
    # self.update() - move the Bomb horizontally toward the target if it
    #                   is being fired.
    def update(self):
        if self.shooting:                                   
            self.rect.centerx += self.dx

    # self.reset() - Hide the bomb offstage with a speed of 0.  It is 
    #                  finished being shot.
    def reset(self):
        self.rect.center = (-100, -100)    # This location is off-screen!
        self.dx = 0
        self.shooting = False

            
##############################################################################
# A Label is used to render text on the screen.  When constructed
#         the following parameters are specified:
#              msg - the text to render on the label.
#              pos - the coordinates of the top-left corner of the label.
#              font - the font file or None.
#              size - the size of the font.
#              color - the color of the text on the label.
class Label(pygame.sprite.Sprite):

    def __init__(self, msg, pos, font, size, color):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(font, size)
        self.text = msg
        self.center = pos
        self.textColor = color

    # self.update() - Render the text on the label.
    def update(self):
        self.image = self.font.render(self.text, 1, self.textColor)
        self.rect = self.image.get_rect()
        self.rect.center = self.center


##############################################################################
#   titleScreen() - Display a title screen and instructions.
#                    The screen stays displayed until the
#                    user clicks the mouse to start the game.
def titleScreen(background):
    
    # Construct labels for a title and game instructions.
    middle = screen.get_width()//2
    titleMsg = Label("Hit the Target", (middle,70), None, 90, FONTCOLOR)
    instr1   = Label("Try to hit the moving target", 
                       (middle,200), None, 45, FONTCOLOR)
    instr2   = Label("You only have "+str(NUMBOMBS)+" tries", 
                       (middle,240), None, 45 ,FONTCOLOR)
    instr3   = Label("Press the space bar to fire the cannon", 
                       (middle,280), None, 45, FONTCOLOR)
    instr4   = Label("Use UP / Down arrows to move the cannon", 
                       (middle,320), None, 45, FONTCOLOR)
    startMsg = Label("Click to start", (middle,420), None, 30,FONTCOLOR)

    # Add the labels to a group  
    labelGroup = pygame.sprite.Group(
                   titleMsg, startMsg, instr1, instr2, instr3, instr4)

    screen.blit(background, (0,0))  # Blit background to screen only once.

    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:  
        clock.tick(30)  # Frame rate 30 frames per second.

        for event in pygame.event.get():      # Handle any events
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN: # Title screen ends
                keepGoing = False                      # when mouse clicked
            elif event.type == pygame.KEYDOWN:         # or ESCAPE or Q pressed
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    keepGoing = False
                                                       
        labelGroup.clear(screen, background)  # Update the display
        labelGroup.update()
        labelGroup.draw(screen)
        
        pygame.display.flip()
                

##############################################################################
#  game() - Play the Hit the Target game.  A player is given NUMBOMBS tries
#           to hit a target with a bomb fired from a cannon.
def game(background):

    background.fill(BACKGROUNDCOLOR)   # Clear the background
    screen.blit(background, (0,0))   # Blit background to screen
    
    # Construct the game entities:
    cannon = Cannon()              # A Cannon object named cannon.  
    target = Target()              # A Target object named target.
    bomb = Bomb()                  # A Bomb object named bomb.
    # A Label object named scoreboard that shows the number of bombs remaining.
    scoreboard = Label("Bombs left: "+str(NUMBOMBS), (100,30), None, 40, FONTCOLOR)
    splatSound = pygame.mixer.Sound("splat.wav")

    # Add the sprites to a group.
    spriteList = [cannon, target, bomb, scoreboard]
    allsprites = pygame.sprite.Group(spriteList)             
        
    clock = pygame.time.Clock()    # A clock for setting a frame rate.
    keepGoing = True               # Signals the game is over.
    win = False                    # Flags game win or loss.
    shooting = False               # Flags a bomb in flight toward target.
    bombs = NUMBOMBS               # Start with an arsenal of bombs.

    while keepGoing:  
        clock.tick(30)             # Frame rate 30 frames per second.

        for event in pygame.event.get():    # Handle any events
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    keepGoing = False
                elif event.key == pygame.K_SPACE:  # Shoot a bomb
                    # Fire the bomb from the position of the cannon,
                    #          but only if there is not already one in flight.
                    if shooting == False:
                        bomb.fire(cannon.get_pos())
                        shooting = True

        # Move the cannon if an up or down arrow key is pressed.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            cannon.moveup()
        elif keys[pygame.K_DOWN]:
            cannon.movedown()

        # Check if the bomb hits the target.  If yes, signal a win, end
        #             the game, and move the bomb offstage.
        if pygame.sprite.collide_rect(bomb, target) :
            splatSound.play()  # make a sound!
            win = True
            keepGoing = False
            bomb.reset()

        # Check if the bomb missed the target (i.e. if it went off the right 
        #             side of the screen.  If it missed, update the count of 
        #             remaining bombs and move the bomb sprite offstage by
        #             calling its reset() method.                    
        if bomb.rect.left >= screen.get_width() :
            shooting = False
            bombs -= 1
            scoreboard.text =  "Bombs left: "+ str(bombs)  # Update the scoreboard
            bomb.reset()
        
        # Check if all bombs are used up. If so, the player has not won the game.
        if bombs <= 0 :
            keepGoing = False

        allsprites.clear(screen, background)
        allsprites.update()
        allsprites.draw(screen)                                        

        pygame.display.flip()

    return win
    
                
##############################################################################
# msgScreen() - Display a message at end of play for 1.5 seconds.
def msgScreen(background, message):
    
    background.fill(BACKGROUNDCOLOR)   # Clear the background
    screen.blit(background, (0,0))     # Blit background to screen only once.

    # Construct a Label object to display the message and add it to a group.
    position = (screen.get_width()//2, screen.get_height()//3)
    msgLabel = Label(message, position, None, 45, FONTCOLOR)
    msgGroup = pygame.sprite.Group( msgLabel )

    clock = pygame.time.Clock()
    keepGoing = True
    frames = 0                  # 1.5 seconds will be 45 frames

    while keepGoing:
    
        clock.tick(30)          # Frame rate 30 frames per second.

        frames = frames + 1     # Count the number of frames displayed

        if frames == 45:        # After 1.5 seconds end the message display
            keepGoing = False 

        for event in pygame.event.get():    # Impatient people can quit earlier
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    keepGoing = False

        msgGroup.clear(screen, background)
        msgGroup.update()
        msgGroup.draw(screen)

        pygame.display.flip()


##############################################################################
# playAgainScreen() - Returns result of True or False depending on user response
def playAgainScreen(background, winLose):

    replay = False   # Default response is not to replay
    
    background.fill(BACKGROUNDCOLOR)   # Clear the background
    screen.blit(background, (0,0))     # Blit background to screen only once.

    # Construct Label objects to display the messages and add them to a group.
    if winLose :
        message1 = "You win!   ;^)"
    else :
        message1 = "You lose...   :-("
        
    position = (screen.get_width()//2, screen.get_height()//3)
    msg1 = Label(message1, position, None, 45, FONTCOLOR)
    message2 = "Do you want to play again? (Y/N)"
    position = (screen.get_width()//2, screen.get_height()//2)
    msg2 = Label(message2, position, None, 45, FONTCOLOR)
    msgGroup = pygame.sprite.Group( msg1, msg2 )

    clock = pygame.time.Clock()
    keepGoing = True
    
    while keepGoing:
    
        clock.tick(30)          # Frame rate 30 frames per second.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    keepGoing = False
                elif event.key == pygame.K_n:  # No, I want to quit!
                    keepGoing = False
                elif event.key == pygame.K_y:  # Yes, I want to play again!
                    keepGoing = False
                    replay = True     

        msgGroup.clear(screen, background)
        msgGroup.update()
        msgGroup.draw(screen)

        pygame.display.flip()

    return replay


##############################################################################
# The main program:
#   Creates the background surface, displays the title/instructions page, runs
#   the main game() function as long as the user wants to keep playing, and
#   then displays the final "The End" message.
def main():
    
    background = pygame.Surface(screen.get_size()) # Construct a background
    background = background.convert()
    background.fill(BACKGROUNDCOLOR)

    titleScreen(background)           # Display title and instructions.

    replay = True
    while replay:
        result = game(background)         # Play the game.

        # Display a win or lose message screen and ask for a replay:
        replay = playAgainScreen(background, result) 
        
    # Final "The End" Screen:
    msgScreen(background, "Thanks for Playing!")
    
##############################################################################
main()                                # Call the main program
pygame.quit()
