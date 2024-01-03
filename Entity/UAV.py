class UAV:

    id = None
    speed = None
    battery = None
    x = None
    y = None
    gfsToVisit = None
    alive = None

    def __init__(self, id=0, battery=100, speed=30, x=1, y=1, gfsToVisit=list(), alive=True):
        self.id = id
        self.battery = battery
        self.speed = speed
        self.x = x
        self.y = y        
        self.gfsToVisit = gfsToVisit
        self.alive = alive