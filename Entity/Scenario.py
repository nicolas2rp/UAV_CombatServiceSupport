from Entity.Threat import *
from Entity.GroundControlStation import *
from Entity.UAV import *
from Entity.GroundForce import *
from Entity.RiskMap import *


class Scenario:

    gcs = None
    gfs = None
    uavs = None
    threats = None
    riskMap = None
    xlim = None
    yLim = None

    def __init__(self,gcs = GroundControlStation(), threats=[Threat()], uavs=[UAV()], gfs=[GroundForce()], riskMap = RiskMap(), xlim=(0,6000), ylim=(0,3000)):
        self.gcs = gcs
        self.threats = threats
        self.uavs = uavs
        self.gfs = gfs
        self.riskMap = riskMap
        self.xlim = xlim
        self.ylim = ylim
