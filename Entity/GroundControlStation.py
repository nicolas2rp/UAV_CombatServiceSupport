import matplotlib.pyplot as plt

class GroundControlStation:

    x = None
    y = None

    def __init__(self,x=1, y=1):
        self.x = x
        self.y = y

    def Plot(self):
        plt.plot(self.x, self.y, '.c', markersize=20) 
        plt.text(self.x - 150, self.y + 150, 'GCS')