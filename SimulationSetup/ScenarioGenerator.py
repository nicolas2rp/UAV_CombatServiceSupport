from Entity.Scenario import *
from Model.SupportMethods import *
class ScenarioGenerator:
        
        scenario = None
        def __init__(self, scenario=Scenario()) :
            self.scenario = scenario
            self.minDistanceGFsGFs = 300
            self.minDistanceGFsThreats = 800
            self.minDistanceGFsGCs = 500
            self.minDistanceThreatsThreats = 2*700
            self.minDistanceThreatsGCS = 700

            self.nThreats = 5

        def CreateScenario(self):
             self._CreateRiskMap()
             self._CreateUAVs()
             self._CreateGFs()
             self._CreateThreats()
             self.scenario.Plot()
    
        def _CreateThreats(self, nThreats=10):
             i = 0
             while i < nThreats:
                x,y = self.__GenerateValidPositionThreats()
                self.scenario.threats.append(Threat(id=i,cx=x,cy=y))
                i +=1

        def _CreateGFs(self, nGFs=10):
            i = 0
            while i < nGFs:
                x,y = self.__GenerateValidPositionGF()
                self.scenario.gfs.append(GroundForce(id=i,x=x, y=y))
                i +=1

        def __GenerateValidPositionThreats(self):
            xlim = self.scenario.xlim
            ylim = self.scenario.ylim
            gcs_x = self.scenario.gcs.x
            gcs_y = self.scenario.gcs.y
            gfs = self.scenario.gfs
            threats = self.scenario.threats
            x0 = -1
            y0 = -1
            i = 500
            while True: #and i > 0:
                valid = True
                x0,y0 = GenerateRandomPosition(xlim, ylim)
                if EuclidianDistance(x0,y0,gcs_x,gcs_y) < self.minDistanceThreatsGCS:
                    continue
                for gf in gfs:
                    if EuclidianDistance(x0,y0,gf.x,gf.y) < self.minDistanceGFsThreats:
                        valid = False
                        break
                for threat in threats:
                    if EuclidianDistance(x0,y0,threat.cx,threat.cy) < threat.detectionRange:
                        valid = False
                        break
                if valid:
                    break
                i-=1
            return x0,y0

        def __GenerateValidPositionGF(self):
            xlim = self.scenario.xlim
            ylim = self.scenario.ylim
            gcs_x = self.scenario.gcs.x
            gcs_y = self.scenario.gcs.y
            gfs = self.scenario.gfs
            x0 = -1
            y0 = -1
            i = 500
            while True and i > 0:
                valid = True
                x0,y0 = GenerateRandomPosition(xlim, ylim)
                if EuclidianDistance(x0,y0,gcs_x,gcs_y) < self.minDistanceGFsGCs:
                    continue
                for gf in gfs:
                    if EuclidianDistance(x0,y0,gf.x,gf.y) < self.minDistanceGFsGFs:
                        valid = False
                        break
                if valid:
                    break
                i-=1
            return x0,y0

        def _CreateUAVs(self, nUAvs=5):
            for i in range(nUAvs):
                self.scenario.uavs.append(UAV(id=i))

        def _CreateRiskMap(self, cellWidth=100, cellHeight=100):
            
            xLength = self.scenario.xlim[1] - self.scenario.xlim[0]
            yLength = self.scenario.ylim[1] - self.scenario.ylim[0]

            nHCells = int(xLength / cellWidth)
            nVCells = int(yLength / cellHeight)
            nCells =  nHCells * nVCells
            xRatio = cellWidth / 2
            yRatio = cellHeight / 2

            self.scenario.riskMap.cx = np.zeros(nCells)
            self.scenario.riskMap.cy = np.zeros(nCells)
            self.scenario.riskMap.risk = np.zeros(nCells)
            i = 0
            index = 0
            
            while i < nHCells:
                j = 0
                while j < nVCells:
                    self.scenario.riskMap.cx[index] = xRatio*(i+1)
                    self.scenario.riskMap.cy[index] = yRatio*(j+1)
                    self.scenario.riskMap.risk[index] = 50
                    index+=1                    
                    j+=1
                i+=1

                