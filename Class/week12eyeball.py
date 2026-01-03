#I Import and initialize
import pygame
pygame.init()
fonts = pygame.font.get_fonts()

WIDTH = 800
HEIGHT = 600


#D Display configuration
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doom Reload")
screen.fill((0,255,0))

#A Action (subdivided into ALTER steps)
clock = pygame.time.Clock()
keepGoing = True


#L Set up main Loop
while keepGoing:
    #T Timer to set frame rate
    clock.tick(30)


    #E Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

    points = ((100,50), (300,50), (350,150), (50,50))
    pygame.draw.circle(screen, (255,255,255), (400,300), 50)
    pygame.draw.circle(screen, (0,255,255), (400,300), 30)
    pygame.draw.circle(screen, (0,0,0), (400,300), 12)
            
    #R Refresh display
    screen.blit(screen,(0,0))
    pygame.display.flip()