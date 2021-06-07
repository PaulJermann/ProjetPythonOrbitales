import numpy
from mayavi import mlab
a0=0.52

nom = input("nom: ")

r = lambda x,y,z: numpy.sqrt(x**2+y**2+z**2)
theta = lambda x,y,z: numpy.arccos(z/r(x,y,z))
phi = lambda x,y,z: numpy.arctan(y/x)

rad2py = lambda r:((1/a0)**(3/2))*(1/(2*numpy.sqrt(6)))*(r/a0)*numpy.exp(-(r/(2*a0)))
WF2py = lambda r,theta,phi: rad2py(r)*(numpy.sqrt(3/(4*numpy.pi))*numpy.sin(theta))*numpy.sin(phi)
Prob2py = lambda r,theta,phi: abs(WF2py(r,theta,phi)**2)

rad2px = lambda r:((1/a0)**(3/2))*(1/(2*numpy.sqrt(6)))*(r/a0)*numpy.exp(-(r/(2*a0)))
WF2px = lambda r,theta,phi: rad2px(r)*(numpy.sqrt(3/(4*numpy.pi))*numpy.sin(theta))*numpy.cos(phi)
Prob2px = lambda r,theta,phi: abs(WF2px(r,theta,phi)**2)

x,y,z = numpy.ogrid[-30:30:100j,-30:30:100j,-30:30:100j]

mlab.figure()
mask = 1

if nom == "2py":
    w=Prob2py(r(x,y,z),theta(x,y,z),phi(x,y,z))

if nom == "2px":
    w=Prob2px(r(x,y,z),theta(x,y,z),phi(x,y,z))

mlab.contour3d(w*mask,contours=6,transparent=True)

mlab.colorbar()
mlab.outline()
mlab.show()
