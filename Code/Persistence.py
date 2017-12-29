import numpy as np
import csv

def getAllPlanets():

    def filter(v):
        p=5
        mass = 0.00314647
        radius = 0.091130151
        axis_major = 1
        period = 365
        if (v[0]<mass*5 and v[0]>mass/5 or v[0]==-1) and \
                (v[1]<radius*10 and v[1]>radius/2 or v[1]==-1) and \
                (v[2]<period*10 and v[2]>0) and \
                (v[3]<axis_major*p and v[3]>axis_major/p or v[3]==-1):
            return True
        return False

    labels = []
    values = []
    reader = csv.reader(open('Datasets/exoplanets.csv', 'rb'), delimiter=';')
    for index,row in enumerate(reader):
        if (index>0):
            v = [float(row[i]) for i in range(1,len(row))]
            if (filter(v)):
                labels.append(row[0])
                values.append(v)
    return np.array(values),labels

def getAPlanetsMass():
    labels = []
    values = []
    reader = csv.reader(open('Datasets/exoMass.csv', 'rb'), delimiter=';')
    mass = 0.00314647
    for index,row in enumerate(reader):
        if (index>0):
            if (not row[1]=='-1'):
                row[1] = float(row[1])
                if (row[1]<mass*5 and row[1]>0):
                    labels.append(row[0])
                    values.append([row[1]])
    return np.array(values),labels

def getPlanetsPeriod():
    labels = []
    values = []
    reader = csv.reader(open('Datasets/exoPeriod.csv', 'rb'), delimiter=';')
    p = 365
    for index,row in enumerate(reader):
        if (index>0):
            if (not row[1]=='-1'):
                row[1] = float(row[1])
                if (row[1]<p*5 and row[1]>p/5):
                    labels.append(row[0])
                    values.append([row[1]])
    return np.array(values),labels
