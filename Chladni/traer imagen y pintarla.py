####### Bloque 1

import numpy as np
import matplotlib.pyplot as plt
import cv2
from google.colab import files
from matplotlib.image import imread
#uploaded = files.upload()
imagen_cruda = cv2.imread("ChladniFigures.png")
print(imagen_cruda.shape)
imagen = imagen_cruda
for i in range(1036):
  for j in range(850):
    for k in range(3):
      imagen[i][j][k] = 0 if imagen_cruda[i][j][0] < 100 else 255


queue = []

def es_invalido(pixel):
  return pixel[0] != pixel[1]

def tacho(x,y):
  if x < 0 or x >= 1036 or y < 0 or y >= 850:
    return
  if imagen[x][y][1] == 0:
    return
  imagen[x][y][0] = 255
  imagen[x][y][1] = 0
  imagen[x][y][2] = 0
  queue.append([x+1,y])
  queue.append([x-1,y])
  queue.append([x,y+1])
  queue.append([x,y-1])
  return

queue.append([13,15])
indice = 0
while indice < len(queue):
  tacho(queue[indice][0],queue[indice][1])
  indice += 1

im = np.empty((1036,850))
for i in range(1036):
  for j in range(850):
    if imagen[i][j][0] == 0:
      im[i][j] = 0
    else:
      if imagen[i][j][1] == 0:
        im[i][j] = 150
      else:
        im[i][j] = 255


plt.rcParams["figure.figsize"] = (18,15.5)
plt.imshow(imagen)
plt.show()


####### Bloque 2


pixeles_en_imagen_x = [31,194,362,530,698]
pixeles_en_imagen_y = [53,221,391,559,727,896]
pixeles_en_imagen = []
for i in range(6):
  for j in range(5):
    pixeles_en_imagen.append([pixeles_en_imagen_y[i],pixeles_en_imagen_x[j]])

cuadrado = im
for i in range(1036):
  for j in range(850):
    cuadrado[i][j] = -1

def pinto(x,y,indicee):
  if es_invalido(imagen[x][y]) or cuadrado[x][y] == indicee:
    return
  cuadrado[x][y] = indicee
  queue.append([x+1,y])
  queue.append([x-1,y])
  queue.append([x,y+1])
  queue.append([x,y-1])


for i in range(30):
  queue = [pixeles_en_imagen[i]]
  indice = 0
  while indice < len(queue):
    pinto(queue[indice][0],queue[indice][1],i)
    indice += 1

limites = [[[5000,5000],[0,0]] for _ in range(30)]
for i in range(1036):
  for j in range(850):
    if cuadrado[i][j] != -1:
      limites[int(cuadrado[i][j])][0][0] = min(limites[int(cuadrado[i][j])][0][0],i)
      limites[int(cuadrado[i][j])][0][1] = min(limites[int(cuadrado[i][j])][0][1],j)
      limites[int(cuadrado[i][j])][1][0] = max(limites[int(cuadrado[i][j])][1][0],i)
      limites[int(cuadrado[i][j])][1][1] = max(limites[int(cuadrado[i][j])][1][1],j)

plt.rcParams["figure.figsize"] = (18,15.5)
plt.imshow(cuadrado)
plt.show()


###### Bloque 3


componente = im
for i in range(1036):
  for j in range(850):
    componente[i][j] = -1

def es_limite(pixel):
  return (pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0)

def asigno_componente(x,y,num_comp):
  if componente[x][y] != -1 or imagen[x][y][1] == 0:
    return
  componente[x][y] = num_comp
  queue.append([x+1,y,num_comp])
  queue.append([x-1,y,num_comp])
  queue.append([x,y+1,num_comp])
  queue.append([x,y-1,num_comp])

for t in range(30):
  contador = -1
  for i in range(limites[t][0][0],limites[t][1][0]+1):
    for j in range(limites[t][0][1],limites[t][1][1]+1):
      if componente[i][j] == -1 and imagen[i][j][1] == 255:
        indice = 0
        contador += 1
        queue = [[i,j,contador*20]]
        while indice < len(queue):
          asigno_componente(queue[indice][0],queue[indice][1],queue[indice][2])
          indice += 1



plt.rcParams["figure.figsize"] = (18,15.5)
# plt.imshow(imagen_purgada[33:168])
plt.imshow(componente)
plt.show()
