import pygame
import random


# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Example")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50, 50))
        self.image = pygame.image.load("mario.png")
        #self.image.fill(YELLOW)
        self.image = pygame.transform.scale(self.image, (60, 40) )
        self.image = self.image.convert()
        self.image.set_colorkey( self.image.get_at((1, 1)) )
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("coin.jpeg")
        self.image = pygame.transform.scale(self.image, (60, 40) )
        self.image = self.image.convert()
        self.image.set_colorkey( self.image.get_at((1, 1)) )
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy.jpeg")
        self.image = pygame.transform.scale(self.image, (60, 40) )
        self.image = self.image.convert()
        self.image.set_colorkey( self.image.get_at((1, 1)) )
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))

# Function to display text on the screen
def draw_text(text, font, color, surface, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# Main game function
def main():
    player = Player()
    coins = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    all_sprites.add(player)

    # Create coins
    for _ in range(10):
        coin = Coin()
        coins.add(coin)
        all_sprites.add(coin)

    # Create enemies
    for _ in range(5):
        enemy = Enemy()
        enemies.add(enemy)
        all_sprites.add(enemy)

    clock = pygame.time.Clock()

    score = 0

    # Timer variables
    start_time = pygame.time.get_ticks()
    countdown_time = 30  # 30 seconds

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update player
        player.update()

        # Check for collision with coins
        coins_collected = pygame.sprite.spritecollide(player, coins, True)
        for coin in coins_collected:
            print("Coin collected!")
            score += 10  # Increment score for each coin collected

        # Check if all coins are collected
        if len(coins) == 0:
            print("You win!")
            running = False

        # Check for collision with enemies
        enemies_hit = pygame.sprite.spritecollide(player, enemies, False)
        if enemies_hit:
            print("Game over!")
            running = False

        # Calculate time remaining
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        time_remaining = countdown_time - elapsed_time
        if time_remaining <= 0:
            print("Time's up!")
            running = False

        # Draw everything
        screen.fill(WHITE)
        all_sprites.draw(screen)

        # Draw score
        draw_text("Score: " + str(score), pygame.font.Font(None, 36), BLACK, screen, 10, 10)

        # Draw timer
        draw_text("Time: " + str(time_remaining), pygame.font.Font(None, 36), BLACK, screen, 10, 50)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
