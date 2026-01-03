import pygame
pygame.init()

# Define colors
green = (0, 255, 0)
white = (255, 255, 255)
cyan = (0, 255, 255)
black = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Static Eye')

# Initial positions
start_x = 400
start_y = 300
move_x = 0


# Eye properties
eye_white_radius = 50
iris_radius = int(eye_white_radius * 0.6)
pupil_radius = int(iris_radius * 0.4)


clock = pygame.time.Clock()
keepGoing = False

# Event loop
while not keepGoing:

    clock.tick(30)

    start_x += move_x

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                     move_x = -5
                if event.key == pygame.K_RIGHT:
                     move_x = 5
        if event.type == pygame.KEYUP:
             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                  move_x = 0

    # Fill the background
    screen.fill(green)

    # Draw the white eye
    pygame.draw.circle(screen, white, (start_x, start_y), eye_white_radius)

    # Draw the iris
    pygame.draw.circle(screen, cyan, (start_x, start_y), iris_radius)

    # Draw the pupil
    pygame.draw.circle(screen, black, (start_x, start_y), pupil_radius)

  
    # Update the display
    pygame.display.flip()
    

# Quit the game
pygame.quit()
quit()
