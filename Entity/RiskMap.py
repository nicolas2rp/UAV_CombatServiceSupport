import numpy as np

class RiskMap:

    cx = None
    cy = None
    risk = None
    cellWidth = None
    cellHeight = None

    def __init__(self,x=np.array([]), y=np.array([]), risk=np.array([]), cellWidth=3, cellHeight=3):
        self.cx = x
        self.cy = y
        self.risk = risk
        self.cellWidth = cellWidth
        self.cellHeight = cellHeight


    