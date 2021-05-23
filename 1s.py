import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d  # Fonction pour la 3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def Radial(x,y,z):
    r=np.sqrt(x**2+y**2+z**2)
    a0=5.245
    R=(1/a0)**(3/2)*2*np.exp(-r/a0)
    return(R)

Y=(1/np.sqrt(4*np.pi))

dz=0.5
zmin=0
zmax=20
x = np.arange(zmin,zmax,dz)
y = np.arange(zmin,zmax,dz)
z = np.arange(zmin,zmax,dz)
X,Y,Z = np.meshgrid(x,y,z)

R=Radial(x,y,z)

graphX = np.arange(0,40)
graphY = R
plt.title("Matplotlib demo")
plt.xlabel("graphX")
plt.ylabel("graphY")
plt.plot(graphX,graphY)
plt.show()
