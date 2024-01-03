from Entity.Threat import *
from Entity.GCS import *
from Entity.UAV import *
from Entity.GF import *
from Entity.RiskMap import *


class Scenario:

    gcs = None
    gfs = None
    uavs = None
    threats = None
    riskMap = None

    def __init__(self,gcs = GCS(), threats=[Threat()], uavs=[UAV()], gfs=[GF()], riskMap = RiskMap()):
        self.gcs = gcs
        self.threats = threats
        self.uavs = uavs
        self.gfs = gfs
        self.riskMap = riskMap
        
