import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mouse Click Example")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initial position and dimensions of the rectangle
rect_x, rect_y = width // 2, height // 2
rect_width, rect_height = 50, 50

# Initial color of the rectangle
rect_color = RED

# Set up the clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if rect_color == BLUE:
                    rect_color = RED
                else:
                    rect_color = BLUE


    # Ensure the rectangle stays within the screen boundaries
    #rect_x = max(0, min(width - rect_width, rect_x))

    # Clear the screen
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
