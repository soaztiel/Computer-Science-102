import pygame as pygame

pygame.init()

w, h = 800, 900
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("LEGO Movie")

blue = (35, 120, 220)
yellow = (255, 220, 0)
brown = (140, 75, 20)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (180, 180, 180)
red = (230, 20, 20)
pink = (255, 105, 180)
orange = (255, 140, 40)
purple = (150, 0, 200)

screen.fill(blue)

pygame.draw.rect(screen, gray, (50, 500, 120, 400))
pygame.draw.rect(screen, gray, (200, 450, 150, 450))
pygame.draw.rect(screen, gray, (400, 480, 180, 420))
pygame.draw.rect(screen, gray, (620, 520, 130, 380))


for x in range(65, 150, 30):
    for y in range(520, 850, 40):
        pygame.draw.rect(screen, white, (x, y, 15, 15))

for x in range(220, 330, 30):
    for y in range(470, 850, 40):
        pygame.draw.rect(screen, white, (x, y, 15, 15))

pygame.draw.rect(screen, red, (650, 100, 20, 300))       
pygame.draw.rect(screen, red, (600, 80, 160, 20))         
pygame.draw.line(screen, white, (680, 120), (720, 400), 4)  
pygame.draw.rect(screen, gray, (700, 400, 40, 40))        

title_font_big = pygame.font.Font(None, 80)
title_font_small = pygame.font.Font(None, 40)

title1 = title_font_big.render("THE", True, white)
title2 = title_font_big.render("LEGO", True, red)
title3 = title_font_big.render("MOVIE", True, white)

screen.blit(title1, (60, 40))
screen.blit(title2, (60, 100))
screen.blit(title3, (60, 160))


pygame.draw.rect(screen, yellow, (275, 250, 250, 250))

pygame.draw.rect(screen, brown, (275, 250, 250, 60))

pygame.draw.circle(screen, black, (340, 350), 22)
pygame.draw.circle(screen, black, (460, 350), 22)

pygame.draw.arc(screen, black, (330, 360, 150, 120), 3.14, 0, 5)

pygame.draw.rect(screen, orange, (275, 500, 250, 300))
pygame.draw.rect(screen, white, (295, 540, 210, 110))
pygame.draw.rect(screen, white, (295, 670, 210, 60))

pygame.draw.rect(screen, yellow, (275, 500, 30, 200))
pygame.draw.rect(screen, yellow, (495, 500, 30, 200))

pygame.draw.rect(screen, purple, (150, 600, 80, 180))
pygame.draw.circle(screen, purple, (190, 600), 40)

pygame.draw.line(screen, pink, (170, 590), (210, 650), 6)

pygame.draw.rect(screen, black, (570, 600, 90, 180))
pygame.draw.circle(screen, black, (615, 600), 45)

pygame.draw.polygon(screen, black, [(600, 550), (610, 570), (590, 570)])
pygame.draw.polygon(screen, black, [(630, 550), (620, 570), (650, 570)])

pygame.display.flip()
pygame.image.save(screen, "lego_movie_poster.png")

# Basic event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
