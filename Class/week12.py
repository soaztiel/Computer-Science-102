#I Import and initialize
import pygame
pygame.init()
fonts = pygame.font.get_fonts()

WIDTH = 640
HEIGHT = 480


#D Display configuration
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doom Reload")

#E Entities (just background for now)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
pygame.draw.line(background, (200, 250, 74), (0,0), (300,300), 1)



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
    pygame.draw.rect(background, (0,0,255), (200, 150, 100, 100))
    pygame.draw.lines(background, (255,0,0), True, ((200,50), (300,50), (250,100)))
    pygame.draw.line(background, (0,0,0), (75,50), (150,50), 5)
    pygame.draw.circle(background, (0,255,0), (110,200), 50)
    pygame.draw.polygon(background, (0,0,0), ((350,300), (450,300),(400,200)))
            
    #R Refresh display
    screen.blit(background,(0,0))

    pygame.display.flip()