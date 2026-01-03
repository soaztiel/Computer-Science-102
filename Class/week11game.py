import pygame
import random
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doom Reloaded")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((235,240,0))

box = pygame.Surface((50,50))
box = box.convert()
box.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

clock = pygame.time.Clock()
keepGoing = True
boxLeftX = 0
boxTopY = 200
dx = 10
dy = 10

while keepGoing:
    clock.tick(30)

    boxLeftX = boxLeftX + dx
    boxTopY = boxTopY + dy

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
    screen.blit(background,(0,0))
    screen.blit(box,(boxLeftX,boxTopY))

    boxLeftX += dx
    boxTopY += dy
    
    if boxTopY > screen.get_height() or boxTopY < 0:
        dy -= dy
    if boxLeftX > screen.get_width() or boxLeftX < 0:
        dx -= dx

    pygame.display.flip()