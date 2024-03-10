import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Dwunastokąt foremny")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)
CZARNY = (0,0,0)


win.fill(JASNY_NIEBIESKI)
pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        pygame.draw.circle(win,CZARNY,(300,300),200,0)
        pygame.draw.rect(win, ZOLTY, (195, 195, 210, 210))



    pygame.display.update()