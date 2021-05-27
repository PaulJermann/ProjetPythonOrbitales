import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

def Radial(x,y,z):
    r=np.sqrt(x**2+y**2+z**2)
    a0=5.245
    R=(1/a0)**(3/2)*(1/(2*np.sqrt(2)))*(2-(r/a0))*np.exp(-r/(2*a0))
    return(R)


dz=0.5
zmin=0
zmax=20
x = np.arange(zmin,zmax,dz)
y = np.arange(zmin,zmax,dz)
z = np.arange(zmin,zmax,dz)
X,Y,Z = np.meshgrid(x,y,z)

R=Radial(x,y,z)
a0=5.245

graphX = (np.arange(0,40))/a0
graphY = (R**2)*(graphX**2)*a0
plt.title("Matplotlib demo")
plt.xlabel("graphX")
plt.ylabel("graphY")
plt.plot(graphX,graphY)
plt.show()