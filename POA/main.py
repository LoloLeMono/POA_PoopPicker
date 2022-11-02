import numpy as np
import random

# n obstacle pour une matrice n*n
#ToDO : Corriger dépassement tab

#1 = caca
#2 = obstacle
#3 = recipe

# Priorité = haut > droite > gauche > bas

h = 5
nbCacas = 3
#capacity = 3
container = 0
end = False
pos = np.array([0, 0])


# Retourne la direction d'un caca
def check(pos):
  scanX = pos[0]
  scanY = pos[1]
  print("Avant de checker haut : ", scanY)

  # tant qu'on ne tombe pas sur un obstacle && on depasse pas en haut
  while scanY >= 0 and mape[scanX][scanY] != 2:
    if mape[scanX][scanY] == 1:  # si on trouve un caca
      return "up"
    else:  # on reagrde vers le haut
      scanY -= 1

  scanX = pos[0]
  scanY = pos[1]
  print("Avant de checker droite : ", scanX)

  # tant qu'on ne tombe pas sur un obstacle && on dépasse pas à droite
  while scanX < h and mape[scanX][scanY] != 2:
    if mape[scanX][scanY] == 1:  # si on trouve un caca
      return "right"
      # go to
    else:  # on regarde vers la droite
      scanX += 1

  scanX = pos[0]
  scanY = pos[1]
  print("Avant de checker gauche : ", scanX)

  # tant qu'on ne tombe pas sur un obstacle et on dépasse pas à gauche
  while scanY >= 0 and mape[scanX][scanY]:
    if mape[scanX][scanY]:  # si on trouve un caca
      return "left"
      # go to
    else:  # on regarde vers la gauche
      scanX -= 1

  scanX = pos[0]
  scanY = pos[1]
  print("Avant de checker bas : ", scanY)

  # tant qu'on ne tombe pas sur un obstacle et on depasse pas en bas
  while scanY < h and mape[scanX][scanY] != 2:
    if mape[scanX][scanY] == 1:  # si on trouve un caca
      return "down"
      # go to
    else:  # on regarde vers le bas
      scanY += 1

  return "null"


# move : Incremente pos dans une direction sinon avance en suivant les priorités
def move(direction):
  if (direction == "up"):
    pos[1] -= 1

  if (direction == "right"):
    pos[0] += 1

  if (direction == "left"):
    pos[0] -= 1

  if (direction == "down"):
    pos[1] += 1



# spawn : Initialise pos au recipe le plus proche et retourne 0
def spawn():
  i = 0
  j = 0

  for i in range(0, h - 1):
    for j in range(0, h - 1):
      if mape[i][j] == 3:
        pos[0] = i
        pos[1] = j
        print("Spawn en ", pos)

        return 0


mape = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])


# fillMap : Construit la map
def fillMape():
  # Remplir les obstacle (2)
  for i in range(h):

    randX = random.randint(0, h - 1)
    randY = random.randint(0, h - 1)

    mape[randX][randY] = 2

  # Ajoute les cacas (1)
  for i in range(nbCacas):

    randX = random.randint(0, h - 1)
    randY = random.randint(0, h - 1)

    while mape[randX][randY] != 0:
      randX = random.randint(0, h - 1)
      randY = random.randint(0, h - 1)

    mape[randX][randY] = 1

  nbRecipes = int(((h * h) / 25) + 1)

  # Ajoute les recipes (3)
  for i in range(nbRecipes):
    randX = random.randint(0, h - 1)
    randY = random.randint(0, h - 1)

    while mape[randX][randY] != 0:
      randX = random.randint(0, h - 1)
      randY = random.randint(0, h - 1)

    mape[randX][randY] = 3

  print(mape)


#
#------------EXECUTION---------------
fillMape()
spawn()

# 10 déplacements
for i in range(0, 10):
  move(check(pos))
  print(pos)
  if (mape[pos[0], pos[1]] == 1):
    print("Un caca trouvé à la case ", pos[0], pos[1], ", miam ^^")
