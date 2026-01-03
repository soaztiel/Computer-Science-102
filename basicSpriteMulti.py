""" basicSpriteMulti.py - works just like moveBox.py but now uses a Sprite """

from random import randint
import pygame
pygame.init()

SQ_SIZE = 30
SQ_MID = SQ_SIZE // 2

WIDTH = 1200
HEIGHT = 900

SQ_CLR = (255,0,0)

NUM_SQUARES = 100     # How many sprites do we want?
MAX_SPEED = 10

screen = pygame.display.set_mode( (WIDTH,HEIGHT) )  # screen is a global variable.

class Square(pygame.sprite.Sprite):

    def __init__(self, yPos, xSpeed):
        pygame.sprite.Sprite.__init__(self)    # Initialize the sprite.
        self.image = pygame.Surface((SQ_SIZE,SQ_SIZE)) # Construct a Surface.
        self.image = self.image.convert()
        self.image.fill(SQ_CLR)                # Color the surface.
                                               
        self.rect = self.image.get_rect()      # Get the Surface's Rectangle.
        self.rect.centerx = 0                  # Start at left window edge.
        self.rect.centery = yPos               # yPos is a parameter.
        self.dx = xSpeed                       # xSpeed is a parmameter.
        self.dy = 0                            # No vertical motion.

    def update(self):
        self.rect.centerx = self.rect.centerx + self.dx  # Move the square ...
        if self.rect.left > screen.get_width():  
            self.rect.right = 0                # ... wrap it back on the screen.
            
            
def main():
    pygame.display.set_caption("basic sprite demo")
    

    # Construct a bunch of Square objects at different speeds and locations.
    squareList = []
    for i in range(NUM_SQUARES) :
        yPosition = randint(0, screen.get_height()) # Pick a random Y coordinate
        xSpeed = randint(1, MAX_SPEED)              # Pick a random speed (pixels per tick)
        squareList.append( Square(yPosition, xSpeed) )                   #   ... and add it to the list of objects
    

    # Put all the Squares into a sprite group
    allSprites = pygame.sprite.Group(squareList)
    
    clock = pygame.time.Clock()
    keepGoing = True
    
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    keepGoing = False
                    
        # Any other game play would go here, inside the game loop
                
        screen.fill((0,0,139))
        allSprites.update()                   # Update the sprites.
        allSprites.draw(screen)               # Draw sprites on the screen.
        
        pygame.display.flip()                 # Make it visible.

main()
pygame.quit()
