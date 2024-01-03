class Threat:

    cx = None
    cy = None
    radius = None
    
    def __init__(self,x=0, y=0, radius=0):
        self.cx = x
        self.cy = y
        self.radius = radius