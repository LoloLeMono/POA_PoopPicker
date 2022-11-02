import pygame, sys
from constant import *

pygame.init()

screen = pygame.display.set_mode([largeur,longueur])

def grille():
    global case_nb, rectx, recty, rectx2
    for x in range(1, 5):
        pygame.draw.rect(screen, forest_green, (rectx, 0, 100, 700))
        rectx += 200
        while case_nb != 5:
            pygame.draw.rect(screen, forest_green, (rectx2, recty, 100, 100))
            recty += 200
            case_nb +=1
        case_nb = 0
        rectx2 += 200
        recty = 0
        case_nb += 1
        print(x)
    pygame.draw.rect(screen, forest_green, (rectx, recty, 100, 700))

def board():
    global case_nb, rectx, recty, rectx2
    for x in range(0,5):
        pygame.draw.rect(screen, cobalt_green, (rectx, 0, 67,67))
        rectx +=134 
        
    for y in range(0,5):
        pygame.draw.rect(screen, cobalt_green, (recty, 67, 67,67))
        recty += 134

    rectx = 0    
    for x in range(0,5):
        pygame.draw.rect(screen, cobalt_green, (rectx, 134, 67,67))
        rectx += 134

    recty = 67
    for x in range(0,5):
        pygame.draw.rect(screen, cobalt_green, (recty, 201, 67,67))
        recty += 134

    rectx = 0
    for x in range(0,5):
        pygame.draw.rect(screen, cobalt_green, (rectx, 268, 67,67))
        rectx += 134

    recty = 67
    for x in range(0,5):
        pygame.draw.rect(screen, cobalt_green, (recty, 335, 67,67))
        recty += 134

    rectx = 0
    for x in range(0,5):
        pygame.draw.rect(screen, cobalt_green, (rectx, 402, 67,67))
        rectx += 134

    recty = 67
    for x in range(0,5):
        pygame.draw.rect(screen, cobalt_green, (recty, 469, 67,67))
        recty += 134

    rectx = 0
    for x in range(0,5):
        pygame.draw.rect(screen, cobalt_green, (rectx, 536, 67,67))
        rectx += 134

    recty = 67
    for x in range(0,5):
        pygame.draw.rect(screen, cobalt_green, (recty, 603, 67,67))
        recty += 134



#        while case_nb !=5 :
#            pygame.draw.rect(screen, cobalt_green, (67, 100, 67,67))
 #           recty +=100
  #          case_nb +=1
   #     case_nb = 0

def get_positions(x,y):
    row = y//case
    col = x//case

    return row,col

case_nb = 0
rectx = 0
rectx2 = 100
recty = 67
screen.fill(emerald_green)
board()
running = True
while running : 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    screen.blit(caca, (450,50))
    screen.blit(mur, (150,150))
    pygame.display.update()
    pygame.display.flip()

pygame.quit()