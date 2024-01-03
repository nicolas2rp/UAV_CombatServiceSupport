import matplotlib.pyplot as plt


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

    def Plot(self):
        if self.alive:
            plt.plot(self.x, self.y, '.k', markersize=20) 
        else:
            plt.plot(self.x, self.y, '.x', markersize=20) 

        plt.text(self.x - 150, self.y + 150, f'UAV-{self.id}')

