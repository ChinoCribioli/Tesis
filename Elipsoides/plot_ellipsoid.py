# https://stackoverflow.com/questions/7819498/plotting-ellipsoid-with-matplotlib

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def hago_punto(alpha,beta):
    return [rx*np.cos(alpha)*np.sin(beta), ry*np.sin(alpha)*np.sin(beta), rz*np.cos(beta)]

fig = plt.figure(figsize=(16,16))


ax = fig.add_subplot(111, projection='3d')



coefs = (1,1,1)
# coefs = (0.8, 1.5, 10) # Coefficients in a0/c x**2 + a1/c y**2 + a2/c z**2 = 1
rx, ry, rz = 1/np.sqrt(coefs)

u = np.linspace(0, 2 * np.pi, 200)
v = np.linspace(0, np.pi, 200)

x = rx * np.outer(np.cos(u), np.sin(v))
y = ry * np.outer(np.sin(u), np.sin(v))
z = rz * np.outer(np.ones_like(u), np.cos(v))

ax.plot_surface(0.94*x, 0.94*y, 0.94*z,  rstride=4, cstride=4, color='y', alpha=0.7, zorder=1)

max_radius = max(1/np.sqrt(0.8), ry, rz)
for axis in 'xyz':
    getattr(ax, 'set_{}lim'.format(axis))((-max_radius, max_radius))

# ax.quiver(0,0,0,rx,0,0,linestyle='-',color='black',arrow_length_ratio=0.2,linewidths=4)
# ax.quiver(0,0,0,-rx,0,0,linestyle='-',color='black',arrow_length_ratio=0.2,linewidths=4)
# ax.quiver(0,0,0,0,ry,0,linestyle='-',color='black',arrow_length_ratio=0.2,linewidths=4)
# ax.quiver(0,0,0,0,-ry,0,linestyle='-',color='black',arrow_length_ratio=0.2,linewidths=4)
# ax.quiver(0,0,0,0,0,rz,linestyle='-',color='black',arrow_length_ratio=0.2,linewidths=4)
# ax.quiver(0,0,0,0,0,-rz,linestyle='-',color='black',arrow_length_ratio=0.2,linewidths=4)

# plt.show()

v = hago_punto(-2*np.pi/5,np.pi/6)
# v = [1.0478916722339398, 0.2685809528458248, 0.03651690329539095]
# v = [1.1097505478681426, -0.09799427764919946, 0.005988818974585219]

# rrx, rry, rrz = 1/np.sqrt((0.8,1.5,10))
# v[0] /= rrx
# v[1] /= rry
# v[2] /= rrz



# dx = np.cos(2*np.pi/3)
# dy = np.sin(2*np.pi/3)
dx = v[0]
dy = v[1]

vectors=np.array([
    [v[0],v[1],v[2],dx,dy,0],[v[0],v[1],v[2],-dx,-dy,0],
    [v[0],v[1],v[2],dy,-dx,0],[v[0],v[1],v[2],-dy,dx,0],
    # [v[0],v[1],v[2],0,0,1],[v[0],v[1],v[2],0,0,-1]
    ])

for vector in vectors:
    for i in range(3,6):
        vector[i] /= 3

for vector in vectors:
    # vvv = np.array([vector[3],vector[4],vector[5]])
    # vlength=np.linalg.norm(vvv)
    # ax.quiver(vector[0],vector[1],vector[2],vvv[0],vvv[1],vvv[2],
    #         pivot='tail',length=vlength,arrow_length_ratio=0.4,
    #         color='black', linewidths=4)
    vv = [v[0]+vector[3],v[1]+vector[4],v[2]+vector[5]]
    # ax.quiver(0,0,0,vv[0],vv[1],vv[2],linestyle='-',color='black',arrow_length_ratio=0)
    vv /= np.linalg.norm(vv)
    # ax.quiver(0,0,0,vv[0],vv[1],vv[2],linestyle='-',color='black',arrow_length_ratio=0)
    ax.scatter(rx*vv[0],ry*vv[1],rz*vv[2],color='b',alpha=1,s=300)
    # print('[',rx*vv[0],',',ry*vv[1],',',rz*vv[2],']')


ax.scatter(v[0],v[1],v[2],color='r',s=300, zorder=10000)
# ax.scatter(0,0,0,color='black', s=30, linewidths=20)


# fig.savefig('ellipsoid.png',dpi=300)
ax.set_axis_off()
ax.grid(False)

plt.show()
