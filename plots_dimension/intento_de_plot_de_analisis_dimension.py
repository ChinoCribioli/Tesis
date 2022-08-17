import numpy as np 
import matplotlib.pyplot as plt 


promedios = [[18.53, 75.08, 153.56, 237.38, 437.09, 632.89], [20.21, 113.18, 274.39, 474.95, 888.64, 1303.91], [21.85, 164.3, 497.31, 856.0, 1698.15, 2546.43], [22.63, 203.37, 713.35, 1263.74, 2521.37, 3774.08], [23.86, 252.34, 1112.38, 2102.55, 4385.6, 6617.07], [24.04, 288.34, 1455.3, 2873.44, 6352.35, 9629.11]]

plt.rcParams["figure.figsize"] = (10,7)
plt.rcParams["font.size"] = 16


stops = ['$10^{0}$', '$10^{-1}$', '$10^{-2}$', '$10^{-3}$', '$10^{-5}$', '$10^{-7}$']
x = [50,100,200,300,500,700]
y = np.random.uniform(2, 7, len(x))

for k in range(6):
  hago_array = [promedios[i][5-k] for i in range(6)]
  plt.bar(x, hago_array, label = stops[5-k], width = 20)


plt.xticks([0]+x, [0]+x, size = 15)
plt.xlabel("Dimensión", size = 17)
plt.ylabel("Cantidad de Iteraciones", size = 17)
plt.title('Evaluando $\mathcal{I}$ con distintos $\\varepsilon$\n', size = 20)
plt.legend()

#plt.grid()
for i in range(6):
  maxi = 0
  for k in range(6):
    if (promedios[k][5-i]*700)/x[k] > (promedios[maxi][5-i]*700)/x[maxi]:
      maxi = k
  plt.plot([0,700], [0 , (promedios[maxi][5-i]*700)/x[maxi] ], '--', lw=4)
  print("La pendiente de la recta", 6-i, "es:", promedios[maxi][5-i]/x[maxi])


plt.tight_layout()

plt.show()
