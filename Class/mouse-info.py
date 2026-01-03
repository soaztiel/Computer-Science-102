import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mouse Motion Example")


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

screen.fill(WHITE)


# Set up the clock
clock = pygame.time.Clock()

# Main loop
keepGoing = True
clock.tick(30)
while keepGoing:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()  # Get the mouse position
            mouse_rel = pygame.mouse.get_rel()
            buttons = pygame.mouse.get_pressed()  # Get the mouse button state
            print("Mouse position:", mouse_pos)
            print("Mouse distance:",mouse_rel)
            if event.type == pygame.MOUSEBUTTONDOWN:
                color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            #print("Mouse buttons:", buttons)
        
    pygame.draw.rect(screen, color, (mouse_pos[0]))

    # Update the display
    pygame.display.flip()


# Quit Pygame
pygame.quit()
