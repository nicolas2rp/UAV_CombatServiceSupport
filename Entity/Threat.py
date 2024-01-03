import matplotlib.pyplot as plt
from matplotlib.patches import Circle

class Threat:

    id = None
    cx = None
    cy = None
    detectionRange = None
    weaponRange = None
    detected = None


    def __init__(self,id=0, cx=0, cy=0, detectionRange=500.0, weaponRange=500, detected=False):
        self.id = id
        self.cx = cx
        self.cy = cy
        self.detected = detected
        self.detectionRange = detectionRange
        self.weaponRange = weaponRange

    def Plot(self):
        if self.detected:
            plt.plot(self.cx, self.cy, '.k', markersize=20)
            Circle((self.cx,self.cy), self.detectionRange,edgecolor='black')
        else:
            plt.plot(self.cx, self.cy, '.k', markersize=20) 
            c = Circle((self.cx,self.cy), self.detectionRange,facecolor='yellow')
            plt.gca().add_patch(c)

        plt.text(self.cx - 150, self.cy + 150, f'Threat-{self.id}')