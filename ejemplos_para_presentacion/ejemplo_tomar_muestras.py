import numpy as np 
import matplotlib.pyplot as plt 


pocas_x = []
muchas_x = []
pocas_y = []
muchas_y = []

def f(x):
	return 2*np.sin(8*x-0.5)-3*np.cos(3*x)

for i in range(201):
	muchas_x.append(i/200)
	muchas_y.append(f(i/200))
	if i%10 == 0 :
		pocas_x.append(i/200)
		pocas_y.append(f(i/200))



plt.rcParams["figure.figsize"] = (10,7)
plt.rcParams["font.size"] = 16

plt.plot(pocas_x,pocas_y, linewidth=3, c='r')
plt.scatter(pocas_x,pocas_y, linewidth=3, c='black')
plt.plot(muchas_x,muchas_y, linewidth=3, c='blue')

# plt.xlabel("$-\log_{10}(\\varepsilon)$", size = 17)
# plt.ylabel("Pendiente de la recta minimizante", size = 17)
# plt.title('Evaluando las pendientes de la recta según la magnitud de $\\varepsilon$\n', size = 20)


plt.tight_layout()

# plt.savefig('21_muestras.png',dpi=300)

plt.show()
