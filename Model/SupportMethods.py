import numpy as np

def GenerateRandomPosition(xlim, ylim):
    x = np.random.uniform(xlim[0], xlim[1])
    y = np.random.uniform(ylim[0], ylim[1])
    return x,y

def EuclidianDistance(x1,y1, x2, y2):
    dist = np.sqrt(np.power(x1-x2,2) + np.power(y1-y2,2))
    return dist 