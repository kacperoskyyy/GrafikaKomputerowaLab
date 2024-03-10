import pygame
import math
import sys

pygame.init()
szerokosc = 600
wysokosc = 600
win = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption("Dwunastokąt foremny")

CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)
CZARNY = (0, 0, 0)


r = 150
srodek= (szerokosc // 2, wysokosc // 2)

def figura(surface):
    a = []
    for i in range(12):
        kat = math.radians(i * 360 / 12)
        x = srodek[0] + int(r * math.cos(kat))
        y = srodek[1] + int(r * math.sin(kat))
        a.append((x, y))
    
    pygame.draw.polygon(surface, CZERWONY, a, 0)

polygon = pygame.Surface((szerokosc, wysokosc))
figura(polygon)
win.blit(polygon, (0, 0))
pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    scaled = pygame.transform.scale(polygon, (szerokosc * 0.35, wysokosc * 0.35))
                    win.fill(CZARNY)
                    win.blit(scaled, ((szerokosc - scaled.get_width()) // 2, (wysokosc - scaled.get_height()) // 2))
                    pygame.display.flip()
                elif event.key == pygame.K_2:
                    rotated = pygame.transform.rotate(polygon, 45)
                    win.fill(CZARNY)
                    win.blit(rotated, ((szerokosc - rotated.get_width()) // 2, (wysokosc - rotated.get_height()) // 2))
                    pygame.display.flip()
                elif event.key == pygame.K_3:
                    flipped = pygame.transform.flip(polygon,0,1)
                    win.fill(CZARNY)
                    win.blit(flipped,((szerokosc - flipped.get_width()) // 2, (wysokosc - flipped.get_height()) // 2))
                    pygame.display.flip()
                elif event.key == pygame.K_4:
                    scale = pygame.transform.scale_by(polygon,(0.35, 1))
                    rotozoom = pygame.transform.rotozoom(scale, 45, 1)
                    win.fill(CZARNY)
                    win.blit(rotozoom,((szerokosc - rotozoom.get_width()) // 2, (wysokosc - rotozoom.get_height()) // 2))
                    pygame.display.flip()
                elif event.key == pygame.K_5:
                    top_scaled = pygame.transform.scale(polygon, (szerokosc, wysokosc * 0.35))
                    win.fill(CZARNY)
                    win.blit(top_scaled,((szerokosc - top_scaled.get_width()) // 2, 1))
                    pygame.display.flip()
                elif event.key == pygame.K_6:
                    scaled_2 = pygame.transform.scale_by(polygon,(0.35, 1))
                    rotozoom = pygame.transform.rotozoom(scaled_2, 180, 1)
                    win.fill(CZARNY)
                    win.blit(rotozoom,((szerokosc - rotozoom.get_width()) // 2, (wysokosc - rotozoom.get_height()) // 2))
                    pygame.display.flip()
                elif event.key == pygame.K_7:
                    scaled_3 = pygame.transform.scale_by(polygon, (0.5,1))
                    flip = pygame.transform.flip(scaled_3, 1,0)
                    win.fill(CZARNY)
                    win.blit(flip, ((szerokosc - flip.get_width()) // 2, (wysokosc - flip.get_height()) // 2))
                    pygame.display.flip()
                elif event.key == pygame.K_8:
                    scaled_4 = pygame.transform.scale_by(polygon, (1,0.4))
                    rotated_2 = pygame.transform.rotate(scaled_4, -20)
                    win.fill(CZARNY)
                    win.blit(rotated_2, ((szerokosc - rotated_2.get_width()) * 1.2, (wysokosc - rotated_2.get_height()) * 1.5))
                    pygame.display.flip()
                elif event.key == pygame.K_9:
                    scaled_5 = pygame.transform.scale_by(polygon,(0.35, 1))
                    rotozoom = pygame.transform.rotozoom(scaled_5, 90, 1)
                    win.fill(CZARNY)
                    win.blit(rotozoom,((szerokosc - rotozoom.get_width() +250) // 2, (wysokosc - rotozoom.get_height()) //2))
                    pygame.display.flip()
                else:
                    
                    win.fill(CZARNY)
                    figura(win)
                    win.blit(win, (0,0))
                    pygame.display.flip()
                    

    pygame.display.update()