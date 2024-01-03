import numpy as np

class FlightPath:

    x = None
    y = None

    def __init__(self, x=np.array(), y=np.array()):
        self.x = x
        self.y = y

