import matplotlib.pyplot as plt

class GroundForce:

    id = None
    visited = None
    x = None
    y = None

    def __init__(self, id=0, visited=False, x=0, y=0):
        self.id = id
        self.visited = visited
        self.x = x
        self.y = y

    def Plot(self):
        if self.visited:
            plt.plot(self.x, self.y, '.g', markersize=20) 
        else:
            plt.plot(self.x, self.y, '.b', markersize=20) 

        plt.text(self.x - 150, self.y + 150, f'GF-{self.id}')