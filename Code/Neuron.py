import numpy as np

class Neuron:

    w = None
    x = 0
    y = 0
    distanceToWinner = -1

    def __init__(self, n, x, y):
        self.__init_weights(n)
        self.x = x
        self.y = y

    def __init_weights(self,n):
        self.w = np.random.rand(n)

