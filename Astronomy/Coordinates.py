import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

def AltAzDiagram(az,alt) :

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xa  = Arrow3D([0, 1], [0, 0], [0, 0], mutation_scale=20, lw=3, arrowstyle="-|>", color="r")
    ya  = Arrow3D([0, 0], [0, 1], [0, 0], mutation_scale=20, lw=3, arrowstyle="-|>", color="g")
    za  = Arrow3D([0, 0], [0, 0], [0, 1], mutation_scale=20, lw=3, arrowstyle="-|>", color="b")

    phi   = (360-az)/180.*np.pi
    theta = (90-alt)/180.*np.pi
    
    x = np.sin(theta)*np.cos(phi)
    y = np.sin(theta)*np.sin(phi)
    z = np.cos(theta)
    
    va  = Arrow3D([0,x],[0,y],[0,z],mutation_scale=20, lw=3, arrowstyle="-|>")
    
    ts  = _np.pi/2
    te  = 
    
    ax.add_artist(xa)
    ax.add_artist(ya)
    ax.add_artist(za)
    ax.add_artist(va)
    
    ax.plot([-0.9,0.9],[0,0],[0,0],color='r', ls='--')
    ax.plot([0,0],[-0.9,0.9],[0,0],color='g', ls='--')
    ax.plot([0,0],[0,0],[-0.9,0.9],color='b', ls='--')
    
    ax.text(1,0,0, "x (North)", color='red', size=25)
    ax.text(-1,0,0, "x (South)", color='red', size=25)
    ax.text(0,1,0, "y (West)", color='green', size=25)
    ax.text(0,-1,0, "-y (East)", color='green', size=25)
    ax.text(0,0,1, "z (Zenith)", color='blue', size=25)
    ax.text(0,0,-1, "-z (Nadir)", color='blue', size=25)
    
    ax.axis("off")

    plt.show()
