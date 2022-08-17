import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors


promedios = [[1539.09, 2173.56, 1848.87, 1953.77, 1710.65, 1714.53, 1751.67, 1641.32, 1481.19, 1412.78], [1714.41, 2125.04, 1846.59, 2019.34, 1719.31, 2148.43, 1863.23, 1632.94, 1600.14, 1401.38], [1805.59, 1696.72, 2002.91, 2043.25, 1973.74, 1737.02, 1985.11, 1985.26, 1581.72, 1404.07], [1785.97, 2477.42, 2437.75, 2857.57, 2065.51, 2166.62, 2498.67, 1777.99, 1738.89, 1407.67], [2113.63, 2217.03, 2107.82, 2266.09, 2229.08, 2023.54, 1906.62, 1734.99, 1513.23, 1406.81], [2234.35, 1969.86, 2115.46, 2192.75, 2221.74, 1957.29, 2169.77, 2209.0, 1660.85, 1399.16], [2400.75, 2648.47, 2012.65, 2259.29, 2174.12, 2452.47, 1953.3, 1913.76, 1749.31, 1402.19], [2366.98, 2336.9, 2654.84, 2232.11, 2800.09, 2508.83, 2044.83, 2000.6, 1548.62, 1402.5], [2270.33, 2331.23, 2550.49, 2221.27, 2255.73, 2402.75, 2515.7, 2038.63, 1566.59, 1401.02]]

cant_de_muestras = [120,250,500,1000,2000,5000,10000,50000,100000]
componentes = [i+1 for i in range(10)]

promedios.reverse()
cant_de_muestras.reverse()

promedios_de_iteraciones = np.array(promedios)


fig, ax = plt.subplots(figsize=(10, 10))
im = ax.imshow(promedios_de_iteraciones, cmap = 'copper')

# We want to show all ticks...
ax.set_xticks(np.arange(len(componentes)))
ax.set_yticks(np.arange(len(cant_de_muestras)))
# ... and label them with the respective list entries
ax.set_xticklabels(componentes,fontsize=16)
ax.set_yticklabels(cant_de_muestras,fontsize=16)


# Loop over data dimensions and create text annotations.
for i in range(len(cant_de_muestras)):
    for j in range(len(componentes)):
        text = ax.text(j, i, promedios_de_iteraciones[i, j],
                       ha="center", va="center", color="white",fontsize=12.5)



ax.set_title("Cantidad de iteraciones promedio en los experimentos\n",fontsize=20)
plt.xlabel("Componente",fontsize=19)
plt.ylabel("Cantidad de Muestras",fontsize=19)
fig.tight_layout()
plt.show()
