class Threat:

    xCenter = None
    yCenter = None
    radius = None
    
    def __init__(self,x=0, y=0, radius=0):
        self.xCenter = x
        self.yCenter = y
        self.radius = radius