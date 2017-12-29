import Persistence
from Neuron import Neuron
import math
import numpy as np


def getWinner(neighborhood,inputs):
    winner = None
    minDistance = float("Inf")
    for i in range(outputNeuron):
        for j in range(outputNeuron):
            distance = sum( [( (inputs[x]-neighborhood[i][j].w[x])**2 if not inputs[x]==-1 else 0) for x in range(len(inputs))]  )
            if ( distance < minDistance ):
                minDistance = distance
                winner = neighborhood[i][j]
    return winner, minDistance

def distanceToWinner(neighborhood,winner):
    for i in range(outputNeuron):
        for j in range(outputNeuron):
            neighborhood[i][j].distanceToWinner = math.sqrt( (winner.x-neighborhood[i][j].x)**2 + (winner.y-neighborhood[i][j].y)**2  )

def getSigma(sigma0, n, tau1):
    return sigma0 * (math.exp( (-n/tau1) ))

def getEta(eta0, n, tau2):
    return eta0 * (math.exp( (-n/tau2) ))

def actualizeWeights(neighborhood, sigma, eta, inputs):
    for i in range(outputNeuron):
        for j in range(outputNeuron):
            h = -1*(neighborhood[i][j].distanceToWinner)**2 / (2*sigma**2)
            gamma = np.exp(h) * eta
            neighborhood[i][j].w += gamma * (inputs-neighborhood[i][j].w)

def sumNeighborhoodWeights(neighborhood):
    c = 0
    for i in range(outputNeuron):
        for j in range(outputNeuron):
            c += sum(neighborhood[i][j].w)
    return c

def train():
    # Train
    f = open("Variation.txt", 'w')
    f.write("Weitghs Variation"+"\n")
    var = sumNeighborhoodWeights(neighborhood)
    for n in range(numMaxIterations):
        print "Iteration "+str(n)
        cost = 0
        for x in range(len(trX)):
            inputs = trX[x]
            winner, error = getWinner(neighborhood, inputs)
            distanceToWinner(neighborhood,winner)
            sigma = getSigma(sigma0, n, lambda0)
            eta = getEta(eta0, n, lambda0)
            actualizeWeights(neighborhood, sigma, eta, inputs)
            if sigma < sigma_limit: sigma = sigma_limit
            if eta < eta_limit: eta = eta_limit
        var2 = sumNeighborhoodWeights(neighborhood)
        var = np.sqrt((var2-var)**2)
        print "     Variation: ",var
        if var < 1: break
        f.write(str(var)+"\n")
        var = var2
        f.flush()
    f.close()
    return neighborhood

# TrainingSet
trX, labels = Persistence.getAllPlanets()
print "Number of Planets: "+str(len(trX))
# Number of Neurons
outputNeuron = 30
nInputs = trX.shape[1]
streetSize = outputNeuron

# neighborhood
neighborhood = [ ([Neuron(nInputs,i,j)  for j in range(streetSize)]) for i in range(streetSize)]

# Variables
numMaxIterations = 100
# max distance between neuron
sigma0 = outputNeuron/2
# learning rate variable (0,1)
eta0 = 0.001
eta_limit = 0.01
sigma_limit = 1
lambda0 = numMaxIterations*len(trX)/math.log(sigma0)
neighborhood = train()

import Graphics
Graphics.plotLearningCurve(["Variation.txt"],"Variation")
import Stadistics
Stadistics.printNeighborhood(getWinner,neighborhood,trX,labels,outputNeuron)
