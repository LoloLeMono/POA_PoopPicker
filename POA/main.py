import numpy as np
import random

# n obstacle pour une matrice n*n
#ToDO : Corriger dépassement tab

# Priorité = haut > droite > gauche > back

h = 5
nbCacas = 3
#capacity = 3
container = 0
end = False


def check(pos):
  scanX = pos[0]
  scanY = pos[1]

  while mape[scanX][scanY] != 2:  # tant qu'on ne tombe pas sur un obstacle
    if mape[scanX][scanY] == 1:  # si on trouve un caca
      return "up"
    else:  # on reagrde vers le haut
      scanY -= 1

  scanX = pos[0]
  scanY = pos[1]

  while mape[scanX][scanY] != 2:  # tant qu'on ne tombe pas sur un obstacle
    if mape[scanX][scanY] == 1:  # si on trouve un caca
      return "right"
      # go to
    else:  # on regarde vers la droite
      scanX += 1

  scanX = pos[0]
  scanY = pos[1]

  while mape[scanX][scanY]:  # tant qu'on ne tombe pas sur un obstacle
    if mape[scanX][scanY]:  # si on trouve un caca
      return "left"
      # go to
    else:  # on regarde vers la gauche
      scanX -= 1

  scanX = pos[0]
  scanY = pos[1]

  while mape[scanX][scanY] != 2:  # tant qu'on ne tombe pas sur un obstacle
    if mape[scanX][scanY] == 1:  # si on trouve un caca
      return "down"
      # go to
    else:  # on regarde vers le bas
      scanY += 1


# Avancer


def move(direction):
  if (direction == "up"):
    pos[1] -= 1

  if (direction == "right"):
    pos[0] += 1

  if (direction == "left"):
    pos[0] -= 1

  if (direction == "down"):
    pos[1] += 1


def spawn():
  i, j = 0

  for i in range(0, h - 1):
    for j in range(0, h - 1):
      if mape[i][j] == 3:
        pos[0] = i
        pos[1] = j


pos = [0, 0]
mape = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

# Remplir les obstacle (2)
for i in range(h):

  randX = random.randint(0, h - 1)
  randY = random.randint(0, h - 1)

  mape[randX][randY] = 2

print(mape)

# Ajoute les cacas (1)
for i in range(nbCacas):

  randX = random.randint(0, h - 1)
  randY = random.randint(0, h - 1)

  while mape[randX][randY] != 0:
    randX = random.randint(0, h - 1)
    randY = random.randint(0, h - 1)

  mape[randX][randY] = 1

print(mape)

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

spawn()

# Check : Retourne la direction d'un caca

for i in range(0, 10):
  move(check(pos))
  print(pos)
