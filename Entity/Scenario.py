from Entity.Threat import *
from Entity.GroundControlStation import *
from Entity.UAV import *
from Entity.GroundForce import *
from Entity.RiskMap import *
import matplotlib.pyplot as plt

class Scenario:

    gcs = None
    gfs = None
    uavs = None
    threats = None
    riskMap = None
    xlim = None
    ylim = None

    def __init__(self,gcs = GroundControlStation(), threats=[], uavs=[], gfs=[], riskMap = RiskMap(), xlim=(0,6000), ylim=(0,3000)):
        self.gcs = gcs
        self.threats = threats
        self.uavs = uavs
        self.gfs = gfs
        self.riskMap = riskMap
        self.xlim = xlim
        self.ylim = ylim


    def Plot(self):
        
        #Plot GCS
        self.gcs.Plot()
        #Plot UAVs
        for uav in self.uavs:
            uav.Plot()
        #Plot GFs
        for gf in self.gfs:
            gf.Plot()
        #Plot Threats
        for threat in self.threats:
            threat.Plot()

        plt.show()
        plt.waitkey(-1)