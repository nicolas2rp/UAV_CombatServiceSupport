class Threat:

    id = None
    cx = None
    cy = None
    detectionRange = None
    weaponRange = None

    def __init__(self,id=0, cx=0, cy=0, detectionRange=500, weaponRange=500):
        self.id = id
        self.cx = cx
        self.cy = cy
        self.detectionRange = detectionRange
        self.weaponRange = weaponRange