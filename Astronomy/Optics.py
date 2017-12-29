class Ray :
    def __init__(self, pos, dir, wavelength = 500e-9) :
        self.pos         = pos
        self.dir         = dir
        self.wavelength  = wavelength

class Name : 
    def __init__(self, name) : 
        self.name = name 

    def __repr__(self) :
        return self.name

class Placement :
    def __init__(self, pos, dir) : 
        self.pos = pos
        self.dir = dir

    def __repr__(self) :
        return "Placement(pos="+str(self.pos)+",dir="+str(self.dir)+")"

class Aperture : 
    def __init__(self, size = 50e-3, type = 'circular') :
        self.size = size
        self.type = type

    def __repr__(self) :
        return "Aperture(size="+str(self.size)+",type="+self.type+")"

class Surface(Name) : 
    def __init__(self, placement, aperture, name = 'surface') :
        self.placement = placement
        self.aperture  = aperture
        self.name      = name
        
    def intersect(self, ray) :
        pass

    def refract(self, ray) :
        pass

    def reflect(self, ray) :
        pass

    def interact(self, ray) :
        pass

    def __repr__(self) : 
        return self.name

class SphericalSurface(Surface) :
    def __init__(self, surface, rCurv, name = 'sphericalsurface') :
        self.surface = surface  
        self.rCurv   = rCurv
        self.name    = name
    
class System(list) : 
    def __init__(self) : 
        pass
    
    def draw2D(self) : 
        pass

    def draw3D(self) : 
        pass

    def rayTrace(self, rays) : 
        pass

class Lens(System) : 
    def __init__(self, surface, rCurv1, rCurv2) :
        pass
