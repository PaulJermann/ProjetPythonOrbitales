import numpy
from mayavi import mlab
a0=0.52

nom = input("nom: ")

r = lambda x,y,z: numpy.sqrt(x**2+y**2+z**2)
theta = lambda x,y,z: numpy.arccos(z/r(x,y,z))
phi = lambda x,y,z: numpy.arctan(y/x)

rad1s = lambda r:((1/a0)**(3/2))*2*numpy.exp(-(r/a0))
WF1s = lambda r,theta,phi: rad1s(r)*(1./(numpy.sqrt(4*numpy.pi)))
Prob1s = lambda r,theta,phi: abs(WF1s(r,theta,phi)**2)

rad2s = lambda r:((1/a0)**(3/2))*(1/(2*numpy.sqrt(2)))*(2-(r/a0))*numpy.exp(-(r/(2*a0)))
WF2s = lambda r,theta,phi: rad1s(r)*(1./(numpy.sqrt(4*numpy.pi)))
Prob2s = lambda r,theta,phi: abs(WF1s(r,theta,phi)**2)

rad2py = lambda r:((1/a0)**(3/2))*(1/(2*numpy.sqrt(6)))*(r/a0)*numpy.exp(-(r/(2*a0)))
WF2py = lambda r,theta,phi: rad2py(r)*(numpy.sqrt(3/(4*numpy.pi))*numpy.sin(theta))*numpy.sin(phi)
Prob2py = lambda r,theta,phi: abs(WF2py(r,theta,phi)**2)

rad2px = lambda r:((1/a0)**(3/2))*(1/(2*numpy.sqrt(6)))*(r/a0)*numpy.exp(-(r/(2*a0)))
WF2px = lambda r,theta,phi: rad2px(r)*(numpy.sqrt(3/(4*numpy.pi))*numpy.sin(theta))*numpy.cos(phi)
Prob2px = lambda r,theta,phi: abs(WF2px(r,theta,phi)**2)

rad2pz = lambda r:((1/a0)**(3/2))*(1/(2*numpy.sqrt(6)))*(r/a0)*numpy.exp(-(r/(2*a0)))
WF2pz = lambda r,theta,phi: rad2pz(r)*(numpy.sqrt(3/(4*numpy.pi))*numpy.cos(theta))
Prob2pz = lambda r,theta,phi: abs(WF2pz(r,theta,phi)**2)

rad3s = lambda r:((1/a0)**(3/2))*(1/(9*numpy.sqrt(3)))*(6-((4*r)/a0)+((4*r**2)/9*a0**2))*numpy.exp(-(r/(3*a0)))
WF3s = lambda r,theta,phi: rad3s(r)*(numpy.sqrt(1/(4*numpy.pi)))
Prob3s = lambda r,theta,phi: abs(WF3s(r,theta,phi)**2)

rad3pz = lambda r:((1/a0)**(3/2))*(1/(9*numpy.sqrt(6)))*((2*r)/(3*a0))*(4-((2*r)/(3*a0)))*numpy.exp(-(r/(3*a0)))
WF3pz = lambda r,theta,phi: rad3pz(r)*(numpy.sqrt(3/(4*numpy.pi))*numpy.cos(theta))
Prob3pz = lambda r,theta,phi: abs(WF3pz(r,theta,phi)**2)

rad3dz2 = lambda r:((1/a0)**(3/2))*(1/(9*numpy.sqrt(30)))*((4*r**2)/(9*a0**2))*numpy.exp(-(r/(3*a0)))
WF3dz2 = lambda r,theta,phi: rad3dz2(r)*(numpy.sqrt(5/(16*numpy.pi))*(3*(numpy.cos(theta)**2)-1))
Prob3dz2 = lambda r,theta,phi: abs(WF3dz2(r,theta,phi)**2)

rad3dxy = lambda r:((1/a0)**(3/2))*(1/(9*numpy.sqrt(30)))*((4*r**2)/9*a0**2)*numpy.exp(-(r/(3*a0)))
WF3dxy = lambda r,theta,phi: rad3dxy(r)*(numpy.sqrt(5/(16*numpy.pi))*(numpy.sin(theta))**2*numpy.sin(2*phi))
Prob3dxy = lambda r,theta,phi: abs(WF3dxy(r,theta,phi)**2)

rad3dxz = lambda r: ((1/a0)**(3/2))*(1/(9*numpy.sqrt(30)))*(4*(r**2)/9*(a0**2))*numpy.exp(-(r/(3*a0)))
WF3dxz = lambda r,theta,phi: rad3dxz(r)*(numpy.sqrt(5/(16*numpy.pi))*numpy.cos(phi)*numpy.sin(2*theta))
Prob3dxz = lambda r,theta,phi: abs(WF3dxz(r,theta,phi)**2)

rad3dyz = lambda r:((1/a0)**(3/2))*(1/(9*numpy.sqrt(30)))*((4*r**2)/9*a0**2)*numpy.exp(-(r/(3*a0)))
WF3dyz = lambda r,theta,phi: rad3dyz(r)*(numpy.sqrt(5/(16*numpy.pi))*(numpy.sin(theta))**2*numpy.sin(phi))
Prob3dyz = lambda r,theta,phi: abs(WF3dyz(r,theta,phi)**2)

rad3dx2y2 = lambda r:((1/a0)**(3/2))*(1/(9*numpy.sqrt(30)))*((4*r**2)/9*a0**2)*numpy.exp(-(r/(3*a0)))
WF3dx2y2 = lambda r,theta,phi: rad3dx2y2(r)*(numpy.sqrt(5/(16*numpy.pi))*(numpy.sin(theta))**2*numpy.cos(2*phi))
Prob3dx2y2 = lambda r,theta,phi: abs(WF3dx2y2(r,theta,phi)**2)

x,y,z = numpy.ogrid[-10:10:100j,-10:10:100j,-10:10:100j]

mlab.figure()
mask = 1

if nom == "1s":
    w=Prob1s(r(x,y,z),theta(x,y,z),phi(x,y,z))

if nom == "2s":
    w=Prob2s(r(x,y,z),theta(x,y,z),phi(x,y,z))

if nom == "2py":
    w=Prob2py(r(x,y,z),theta(x,y,z),phi(x,y,z))

if nom == "2px":
    w=Prob2px(r(x,y,z),theta(x,y,z),phi(x,y,z))

if nom == "2pz":
    w=Prob2pz(r(x,y,z),theta(x,y,z),phi(x,y,z))

if nom == "3s":
    w=Prob3s(r(x,y,z),theta(x,y,z),phi(x,y,z))

if nom == "3pz":
    w=Prob3pz(r(x,y,z),theta(x,y,z),phi(x,y,z))

if nom == "3dz2":
    w=Prob3dz2(r(x,y,z),theta(x,y,z),phi(x,y,z))

if nom == "3dxy":
    w=Prob3dyz(r(x,y,z),theta(x,y,z),phi(x,y,z))

if nom == "3dxz":
    w=Prob3dxz(r(x,y,z),theta(x,y,z),phi(x,y,z))

if nom == "3dyz":
    w=Prob3dyz(r(x,y,z),theta(x,y,z),phi(x,y,z))

if nom == "3dx2y2":
    w=Prob3dx2y2(r(x,y,z),theta(x,y,z),phi(x,y,z))

mlab.contour3d(w*mask,contours=6,transparent=True)

mlab.colorbar()
mlab.outline()
mlab.show()
