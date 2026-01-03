#I Import and initialize
import pygame
pygame.init()
fonts = pygame.font.get_fonts()

WIDTH = 1440
HEIGHT = 1440


#D Display configuration
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doom Reload")

#E Entities (just background for now)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
pygame.draw.line(background, (200, 250, 74), (0,0), (300,300), 5)



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
    pygame.draw.rect(background, (0,0,0), (150, 310, 250,100), 5)
    pygame.draw.line(background, (0,50,15), (0,0), (640,480), 20)
    pygame.draw.circle(background, (100,130,30), (200,200), 40)
    pygame.draw.polygon(background, (67,15,78), points, 7)
    myfont = pygame.font.SysFont("Comic Sans MS", 30)
    labelSurface = myfont.render("Hello, world!", 1, (0,0,255))
            
    #R Refresh display
    screen.blit(background,(0,0))
    screen.blit(labelSurface, (425, 275))

    pygame.display.flip()