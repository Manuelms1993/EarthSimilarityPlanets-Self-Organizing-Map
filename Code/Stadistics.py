import numpy as np

def printNeighborhood(getWinner,neighborhood,trX,labels,outputNeuron):

    def selectionsort(distances,labels):
        tam = len(distances)
        for i in range(0,tam-1):
            max=i
            for j in range(i+1,tam):
                if distances[max] < distances[j]:
                    max=j

            aux = distances[max]
            distances[max] = distances[i]
            distances[i] = aux
            aux = labels[max]
            labels[max] = labels[i]
            labels[i] = aux

        return distances,labels

    import matplotlib.pyplot as plt
    plt.figure(num=None, figsize=(15, 8), dpi=60, facecolor='w', edgecolor='k')
    inputs = trX[0]
    earth, error = getWinner(neighborhood, inputs)
    plt.plot(earth.x,earth.y, 'ro', markersize=15)
    plt.text(earth.x,earth.y+0.001, labels[0], fontsize = 12, color='r')
    distances = []
    distances.append(0)
    for i in range(1,len(trX)):
        inputs = trX[i]
        winner, error = getWinner(neighborhood, inputs)
        d = sum((neighborhood[earth.x][earth.y].w-inputs)**2)
        distances.append(d)
        rx = np.random.rand() * 0.1
        ry = np.random.rand() * 0.1
        plt.plot(winner.x+rx,winner.y+ry, 'bo', markersize=5)
        plt.text(winner.x+rx,winner.y+ry, labels[i], fontsize = 10, color='b')
    plt.axis([-1,outputNeuron+1,-1,outputNeuron+1])
    distances = np.array(distances)
    distances, labels = selectionsort(distances,labels)
    f = open("Similarity.txt", 'w')
    for i in range(distances.shape[0]):
        f.write(labels[i]+"\n")
    f.close()
    plt.show()
    print "\nSimilarity.txt created!!"
