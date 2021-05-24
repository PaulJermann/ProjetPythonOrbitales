import numpy
from math import pi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
#on cree plein de valeurs pour faire la grille
dz=0.5
zmin=0
zmax=20
x = np.arange(zmin,zmax,dz)
y = np.arange(zmin,zmax,dz)
z = np.arange(zmin,zmax,dz)
X,Y,Z = np.meshgrid(x,y,z)
#on veut travailler en 3D donc on se place en coordonnées sphériques
r = numpy.sqrt(x ** 2 + y ** 2 + z ** 2)
theta = numpy.arccos(z/r)
phi = numpy.arctan(y/x)
a0 = 0.529 * 10**(-10) #valeur du rayon de Bohr
R = (1/a0)**3/2 * 2 * numpy.exp(-r/a0) # partie radiale 1s
#on calcule la fonction d'onde soit R*Y cf doc
WF = R * 1/(4 * np.pi )
#tracé du résultat en 3D
fig = plt.figure()
ax = fig.gca(projection='3d') # Affichage en 3D
ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0) # Tracé d'une
surface
plt.title("Tracé d'une surface")
graphx = r * np.sin(theta)* np.cos(phi)
graphy = r * np.sin(phi) * np.sin(phi)
graphz = r * np.cos(phi)
ax.set_xlabel('graphx')
ax.set_ylabel('graphy')
ax.set_zlabel('graphz')
plt.tight_layout()
plt.show()