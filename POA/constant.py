import pygame
import os


largeur, longueur = 670,670
lignes, colonnes = 8,8
case = largeur/12



emerald_green = (0,201,87) #emeraldgreen
forest_green = (34,139,34) #forestgreen
cobalt_green = (61,145,64) #cobaltgreen

Path = "images/"
caca = pygame.transform.scale(pygame.image.load(os.path.join(Path,"caca.png")),(case, case))
mur = pygame.transform.scale(pygame.image.load(os.path.join(Path,"mur.jpg")),(case, case))