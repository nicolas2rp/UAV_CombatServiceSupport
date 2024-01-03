from Entity.Scenario import *

class ScenarioGenerator:
        
        scenario = None
        def __init__(self, scenario=Scenario()) :
                self.scenario = scenario


        def CreateScenario(self):
             self._CreateRiskMap()
             self._CreateUAVs()

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

                