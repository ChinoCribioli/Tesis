import numpy as np 
import matplotlib.pyplot as plt 

pendientes = [0.37060000000000004, 1.5016, 3.0712, 4.7495, 9.074785714285715, 13.75587142857143]
indices = [0,1,2,3,5,7]



plt.rcParams["figure.figsize"] = (10,7)
plt.rcParams["font.size"] = 16

plt.plot(indices,pendientes, linewidth=3, c='r')
plt.scatter(indices,pendientes, linewidth=3, c='black')

plt.xlabel("$-\log_{10}(\\varepsilon)$", size = 17)
plt.ylabel("Pendiente de la recta minimizante", size = 17)
plt.title('Evaluando las pendientes de la recta según la magnitud de $\\varepsilon$\n', size = 20)


plt.tight_layout()

plt.show()
