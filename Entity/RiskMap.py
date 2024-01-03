import numpy as np

class RiskMap:

    cells = None
    cellWidth = None
    cellHeight = None

    def __init__(self,cells=np.array([]), cellWidth=3, cellHeight=3):
        self.cells = cells
        self.cellWidth = cellWidth
        self.cellHeight = cellHeight
