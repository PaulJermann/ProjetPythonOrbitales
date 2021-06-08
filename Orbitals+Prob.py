# Our goal is to draw a 3D representation of a few orbitals
# we import two packages we need for our program
import numpy # we use numpy in order to use mathematical tools depending on x, y, z
from mayavi import mlab # we use mlab in order to draw our orbitals
import matplotlib
import matplotlib.pyplot as plt # We import all the modules we need to use in order to draw the graph (probability)
a0=0.52 # we define the Bohr radius
A="Orbital group, for example 3d"

print("This program displays the orbital shape as well as the most probable distance between the electron and the nuclei for a chosen orbital in the hydrogen atom.")

nom = input("Which orbital do you wish to visualize? Please enter the name of the orbital: ") # the user chooses the orbital he wants to draw

# We define the spheric coordinates r, theta, phi depending on x, y, z
r = lambda x,y,z: numpy.sqrt(x**2+y**2+z**2)
theta = lambda x,y,z: numpy.arccos(z/r(x,y,z))
phi = lambda x,y,z: numpy.arctan(y/x)

# We create a register of each equation we need to draw the different orbitals

#1s
rad1s = lambda r:((1/a0)**(3/2))*2*numpy.exp(-(r/a0))
WF1s = lambda r,theta,phi: rad1s(r)*(1./(numpy.sqrt(4*numpy.pi)))
Prob1s = lambda r,theta,phi: abs(WF1s(r,theta,phi)**2)

#2s
rad2s = lambda r:((1/a0)**(3/2))*(1/(2*numpy.sqrt(2)))*(2-(r/a0))*numpy.exp(-(r/(2*a0)))
WF2s = lambda r,theta,phi: rad1s(r)*(1./(numpy.sqrt(4*numpy.pi)))
Prob2s = lambda r,theta,phi: abs(WF1s(r,theta,phi)**2)

#2py
rad2py = lambda r:((1/a0)**(3/2))*(1/(2*numpy.sqrt(6)))*(r/a0)*numpy.exp(-(r/(2*a0)))
WF2py = lambda r,theta,phi: rad2py(r)*(numpy.sqrt(3/(4*numpy.pi))*numpy.sin(theta))*numpy.sin(phi)
Prob2py = lambda r,theta,phi: abs(WF2py(r,theta,phi)**2)

#2px
rad2px = lambda r:((1/a0)**(3/2))*(1/(2*numpy.sqrt(6)))*(r/a0)*numpy.exp(-(r/(2*a0)))
WF2px = lambda r,theta,phi: rad2px(r)*(numpy.sqrt(3/(4*numpy.pi))*numpy.sin(theta))*numpy.cos(phi)
Prob2px = lambda r,theta,phi: abs(WF2px(r,theta,phi)**2)

#2pz
rad2pz = lambda r:((1/a0)**(3/2))*(1/(2*numpy.sqrt(6)))*(r/a0)*numpy.exp(-(r/(2*a0)))
WF2pz = lambda r,theta,phi: rad2pz(r)*(numpy.sqrt(3/(4*numpy.pi))*numpy.cos(theta))
Prob2pz = lambda r,theta,phi: abs(WF2pz(r,theta,phi)**2)

#3s
rad3s = lambda r:((1/a0)**(3/2))*(1/(9*numpy.sqrt(3)))*(6-((4*r)/a0)+((4*r**2)/9*a0**2))*numpy.exp(-(r/(3*a0)))
WF3s = lambda r,theta,phi: rad3s(r)*(numpy.sqrt(1/(4*numpy.pi)))
Prob3s = lambda r,theta,phi: abs(WF3s(r,theta,phi)**2)

#3pz
rad3pz = lambda r:((1/a0)**(3/2))*(1/(9*numpy.sqrt(6)))*((2*r)/(3*a0))*(4-((2*r)/(3*a0)))*numpy.exp(-(r/(3*a0)))
WF3pz = lambda r,theta,phi: rad3pz(r)*(numpy.sqrt(3/(4*numpy.pi))*numpy.cos(theta))
Prob3pz = lambda r,theta,phi: abs(WF3pz(r,theta,phi)**2)

#3dz2
rad3dz2 = lambda r:((1/a0)**(3/2))*(1/(9*numpy.sqrt(30)))*((4*r**2)/(9*a0**2))*numpy.exp(-(r/(3*a0)))
WF3dz2 = lambda r,theta,phi: rad3dz2(r)*(numpy.sqrt(5/(16*numpy.pi))*(3*(numpy.cos(theta)**2)-1))
Prob3dz2 = lambda r,theta,phi: abs(WF3dz2(r,theta,phi)**2)

#3dxy
rad3dxy = lambda r:((1/a0)**(3/2))*(1/(9*numpy.sqrt(30)))*((4*(r**2))/(9*(a0**2)))*numpy.exp(-(r/(3*a0)))
WF3dxy = lambda r,theta,phi: rad3dxy(r)*(numpy.sqrt(5/(16*numpy.pi))*((numpy.sin(theta))**2)*numpy.sin(2*phi))
Prob3dxy = lambda r,theta,phi: abs(WF3dxy(r,theta,phi)**2)

#3dxz
rad3dxz = lambda r: ((1/a0)**(3/2))*(1/(9*numpy.sqrt(30)))*(4*(r**2)/9*(a0**2))*numpy.exp(-(r/(3*a0)))
WF3dxz = lambda r,theta,phi: rad3dxz(r)*(numpy.sqrt(5/(16*numpy.pi))*numpy.cos(phi)*numpy.sin(2*theta))
Prob3dxz = lambda r,theta,phi: abs(WF3dxz(r,theta,phi)**2)

#3dyz
rad3dyz = lambda r: ((1/a0)**(3/2))*(1/(9*numpy.sqrt(30)))*((4*(r**2))/(9*(a0**2)))*numpy.exp(-(r/(3*a0)))
WF3dyz = lambda r,theta,phi: rad3dyz(r)*(numpy.sqrt(5/(16*numpy.pi))*((numpy.sin(theta))*numpy.sin(phi)*numpy.cos(theta)))
Prob3dyz = lambda r,theta,phi: abs(WF3dyz(r,theta,phi)**2)

#3dx2y2
rad3dx2y2 = lambda r:((1/a0)**(3/2))*(1/(9*numpy.sqrt(30)))*((4*r**2)/9*a0**2)*numpy.exp(-(r/(3*a0)))
WF3dx2y2 = lambda r,theta,phi: rad3dx2y2(r)*(numpy.sqrt(5/(16*numpy.pi))*(numpy.sin(theta))**2*numpy.cos(2*phi))
Prob3dx2y2 = lambda r,theta,phi: abs(WF3dx2y2(r,theta,phi)**2)

#we define the grid on which we want to draw the orbitals with one hundred steps
x,y,z = numpy.ogrid[-10:10:100j,-10:10:100j,-10:10:100j]

# we draw the figure
mlab.figure()
mask = 1

# depending on what the orbital the user chooses we draw the corresponding orbital
if nom == "1s":
    w=Prob1s(r(x,y,z),theta(x,y,z),phi(x,y,z))
    A="1s"

if nom == "2s":
    w=Prob2s(r(x,y,z),theta(x,y,z),phi(x,y,z))
    A = "2s"

if nom == "2py":
    w=Prob2py(r(x,y,z),theta(x,y,z),phi(x,y,z))
    A = "2p"

if nom == "2px":
    w=Prob2px(r(x,y,z),theta(x,y,z),phi(x,y,z))
    A = "2p"

if nom == "2pz":
    w=Prob2pz(r(x,y,z),theta(x,y,z),phi(x,y,z))
    A = "2p"

if nom == "3s":
    w=Prob3s(r(x,y,z),theta(x,y,z),phi(x,y,z))
    A = "3s"

if nom == "3pz":
    w=Prob3pz(r(x,y,z),theta(x,y,z),phi(x,y,z))
    A = "3p"

if nom == "3dz2":
    w=Prob3dz2(r(x,y,z),theta(x,y,z),phi(x,y,z))
    A = "3d"

if nom == "3dxy":
    w=Prob3dxy(r(x,y,z),theta(x,y,z),phi(x,y,z))
    A = "3d"

if nom == "3dxz":
    w=Prob3dxz(r(x,y,z),theta(x,y,z),phi(x,y,z))
    A = "3d"

if nom == "3dyz":
    w=Prob3dyz(r(x,y,z),theta(x,y,z),phi(x,y,z))
    A = "3d"

if nom == "3dx2y2":
    w=Prob3dx2y2(r(x,y,z),theta(x,y,z),phi(x,y,z))
    A = "3d"

# the orbital's characteristics
mlab.contour3d(w*mask,contours=20,transparent=False)

mlab.colorbar()
mlab.outline()
mlab.show()

def radial1s(x,y,z):
    r=numpy.sqrt(x**2+y**2+z**2)
    a0=5.29
    R=(1/a0)**(3/2)*2*numpy.exp(-r/a0)
    return(R)

def radial2s(x,y,z) :
    r = numpy.sqrt(x ** 2 + y ** 2 + z ** 2)
    a0 = 5.29
    R = (1/a0) ** (3/2) * (1/ (2 * numpy.sqrt(2))) * (2 - (r / a0)) * numpy.exp(-r / (2 * a0))
    return (R)

def radial2p(x, y,z) :
    r = numpy.sqrt(x ** 2 + y ** 2 + z ** 2)
    a0 = 5.29
    R = (1 / a0) ** (3 / 2) * (1 / (2 * numpy.sqrt(6))) * (r / a0) * numpy.exp(-r / (2 * a0))
    return (R)

def radial3s(x, y,z) :
    r = numpy.sqrt(x ** 2 + y ** 2 + z ** 2)
    a0 = 5.29
    R = ((1 / a0) ** (3 / 2)) * (1 / (9 * numpy.sqrt(3))) * (6 - (4 * r / a0) + (4* r**2 / (9 * a0 **2))) * numpy.exp(-r / (3 * a0))
    return (R)

def radial3pz(x, y,z) :
    r = numpy.sqrt(x ** 2 + y ** 2 + z ** 2)
    a0 = 5.29
    R = ((1 / a0) ** (3 / 2)) * (1 / (9 * numpy.sqrt(6))) * (2 * r /3 * a0) * (4 - 2 * r / (3 * a0)) * numpy.exp(-r / (3 * a0))
    return (R)

def radial3d(x, y,z) :
    r = numpy.sqrt(x ** 2 + y ** 2 + z ** 2)
    a0 = 5.29
    R = (1 / a0) ** (3 / 2) * (1 / (9 * numpy.sqrt(30))) * (4 * r**2 /9 * a0**2) * numpy.exp(-r / (3 * a0))
    return (R)

# we create a grid in order to be able to make a graph, so we define the coordinates and the axis
dz = 0.5
zmin = 0
zmax = 50
x = numpy.arange(zmin, zmax, dz)
y = numpy.arange(zmin, zmax, dz)
z = numpy.arange(zmin, zmax, dz)
X, Y, Z = numpy.meshgrid(x, y, z)

# we start a loop of "if" related to the orbital chosen by the user
# according to the chosen orbital, it will plot the good and perfect graph representing the most probable distance between the electron and the nuclei
if A == "1s" :
    R = radial1s(x,y,z)
    a0 = 5.29
    r = numpy.sqrt(x ** 2 + y ** 2 + z ** 2)
    graphX = r / a0
    graphY = (R ** 2) * (r ** 2) * a0
    plt.title("Probability density of the radial presence times a0 depending on r/a0")
    plt.xlabel("r/a0")
    plt.ylabel("a0Dr")
    plt.plot(graphX, graphY)
    ymax = numpy.max(graphY)
    xmax = graphX[numpy.argmax(graphY)]
    print("xmax =", xmax, "a0")
    plt.scatter(xmax, ymax)
    plt.text(xmax, ymax, " Maximum probability distance : 0.9822594371846185 a0 ")
    plt.show()
    matplotlib.pyplot.close()



elif A == "2s":
    R = radial2s(x,y,z)
    a0 = 5.29
    r = numpy.sqrt(x ** 2 + y ** 2 + z ** 2)
    graphX = r / a0
    graphY = (R ** 2) * (r ** 2) * a0
    plt.title("Probability density of the radial presence times a0 depending on r/a0")
    plt.xlabel("r/a0")
    plt.ylabel("a0Dr")
    plt.plot(graphX, graphY)
    ymax = numpy.max(graphY)
    xmax = graphX[numpy.argmax(graphY)]
    print("xmax =", xmax, "a0")
    plt.scatter(xmax, ymax)
    plt.text(xmax, ymax, "Maximum probability distance : 5.238716998317965 a0 ")
    plt.show()
    matplotlib.pyplot.close()

elif A == "2p":
    R = radial2p(x,y,z)
    a0 = 5.29
    r = numpy.sqrt(x ** 2 + y ** 2 + z ** 2)
    graphX = r / a0
    graphY = (R ** 2) * (r ** 2) * a0
    plt.title("Probability density of the radial presence times a0 depending on r/a0")
    plt.xlabel("r/a0")
    plt.ylabel("a0Dr")
    plt.plot(graphX, graphY)
    ymax = numpy.max(graphY)
    xmax = graphX[numpy.argmax(graphY)]
    print("xmax =", xmax, "a0")
    plt.scatter(xmax, ymax)
    plt.text(xmax, ymax, "Maximum probability distance : 3.929037748738474 a0 ")
    plt.show()
    matplotlib.pyplot.close()

elif A == "3s":
    R = radial3s(x,y,z)
    a0 = 5.29
    r = numpy.sqrt(x ** 2 + y ** 2 + z ** 2)
    graphX = r / a0
    graphY = (R ** 2) * (r ** 2) * a0
    plt.title("Probability density of the radial presence times a0 depending on r/a0")
    plt.xlabel("r/a0")
    plt.ylabel("a0Dr")
    plt.plot(graphX, graphY)
    ymax = numpy.max(graphY)
    xmax = graphX[numpy.argmax(graphY)]
    print("xmax =", xmax, "a0")
    plt.scatter(xmax, ymax)
    plt.text(xmax, ymax, " Maximum probability distance : 13.096792495794915 a0 ")
    plt.show()
    matplotlib.pyplot.close()



elif A == "3p":
    R = radial3pz(x,y,z)
    a0 = 5.29
    r = numpy.sqrt(x ** 2 + y ** 2 + z ** 2)
    graphX = r / a0
    graphY = (R ** 2) * (r ** 2) * a0
    plt.title("Probability density of the radial presence times a0 depending on r/a0")
    plt.xlabel("r/a0")
    plt.ylabel("a0Dr")
    plt.plot(graphX, graphY)
    ymax = numpy.max(graphY)
    xmax = graphX[numpy.argmax(graphY)]
    print("xmax =", xmax, "a0")
    plt.scatter(xmax, ymax)
    plt.text(xmax, ymax, " Maximum probability distance : 11.950823152412857 a0 ")
    plt.show()
    matplotlib.pyplot.close()

elif A == "3d":
    R = radial3d(x,y,z)
    a0 = 5.29
    r = numpy.sqrt(x ** 2 + y ** 2 + z ** 2)
    graphX = r / a0
    graphY = (R ** 2) * (r ** 2) * a0
    plt.title("Probability density of the radial presence times a0 depending on r/a0")
    plt.xlabel("r/a0")
    plt.ylabel("a0Dr")
    plt.plot(graphX, graphY)
    ymax = numpy.max(graphY)
    xmax = graphX[numpy.argmax(graphY)]
    print("xmax =", xmax, "a0")
    plt.scatter(xmax, ymax)
    plt.text(xmax, ymax, "Maximum probability distance : 9.004044840859002 a0 ")
    plt.show()
    matplotlib.pyplot.close()

else: # if the orbital chosen by the user doesn't match with the orbitals of the program, we ask him to enter another orbital which fits in our program
    print("Please restart the program and enter a valid orbital name")


