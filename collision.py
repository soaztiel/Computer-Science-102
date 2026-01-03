import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Collision Detection")

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,0,255)

# Define Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)    # Initialize the sprite.
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 100)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 2
        if keys[pygame.K_RIGHT]:
            self.rect.x += 2
        if keys[pygame.K_UP]:
            self.rect.y -= 2
        if keys[pygame.K_DOWN]:
            self.rect.y += 2

# Define Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)    # Initialize the sprite.
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, 50)

# Create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Create player and enemy instances
player = Player()
enemy = Enemy()

# Add sprites to sprite groups
all_sprites.add(player, enemy)
enemies.add(enemy)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update sprites
    all_sprites.update()
    
    
    
    # Check for collision using spritecollide()
    collisions = pygame.sprite.spritecollide(player, enemies, True)
    if collisions:
        print("Collision detected with spritecollide!")
        running = False

    # Check for collision using colliderect()
    if player.rect.colliderect(enemy.rect):
        print("Collision detected with colliderect!")
        #running = False
    
    # Draw sprites
    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

