from dis import dis
import math
import sys
import numpy as np

class clustering:

    K: int
    M: int

    clusters   = {}
    clusterKey = []
    centroids  = []
    data       = [] 

    def __init__(self) -> None:
        self.getData()

    def getData(self):
        try:
            with open(sys.argv[1], mode = 'r', encoding = 'utf-8') as file:
                lines   = file.readlines()
                self.K  = int(lines[0][0])
                self.M  = int(lines[0][2])
                # Could probably do this without for loops
                for x in range(1,self.K+1):
                    self.centroids.append(
                            list(
                                map(
                                    float,lines[x].split()
                                    )
                                )
                            )
                for x in range(1,len(lines)):
                    self.data.append(
                            list(
                                map(
                                    float,lines[x].split()
                                    )
                                )
                            )
        except IndexError:
            print("Oops! You forgot to input a file name!")
            sys.exit()
        except FileNotFoundError:
            print("Error opening file " + sys.argv[1])
            sys.exit()

    def llyod(self):
        '''
            Centriods to clusters
            - Assign each data point to a centroid based on shortest distance
                - can use distionaries for assignment with centroid as the key
                    - Convert arr val into a string

            Clusters to centroid
            - Compute new centroids from the points in their cluster
                - Find the mean

            if centroids aren't the same run it back
        '''
        # Centroid to cluster
        clusters = dict()
        prevCent = self.centroids[:] # Used to check for change in the centroids later on
        for point in self.data:
            distance = -1
            for centroid in self.centroids:
                if distance == -1:
                    # Initialize distance variable
                    distance = self.getDistance(centroid,point)
                    # Add point to dictionary
                    try:
                        clusters[str(centroid)].append(point)
                    except KeyError: # Initialize centroid in the dictionary
                        clusters[str(centroid)] = []
                        clusters[str(centroid)].append(point)
                elif self.getDistance(centroid,point) < distance:
                    # Update distance
                    distance = self.getDistance(centroid,point)
                    # Remove point from previous cluster
                    for value in clusters.values():
                        if point in value:
                            value.remove(point)
                    # Add point to new cluster
                    try:
                        clusters[str(centroid)].append(point)
                    except KeyError: # Initialize centroid in the dictionary
                        clusters[str(centroid)] = []
                        clusters[str(centroid)].append(point)

        # Cluster to centroid
        for i,centriod in enumerate(self.centroids):
            try:
                self.centroids[i] = np.round(np.mean(clusters[str(centriod)],axis = 0),3)
            except KeyError:
                pass
        if (np.array(prevCent) == np.array(self.centroids)).all():
            # Clusters have been sorted
            self.viewCentroids()
        else:
            self.llyod()  

    def getDistance(self,arr0,arr1) -> float:
        x = np.array(arr0)
        y = np.array(arr1)

        # Point comparison
        z = np.array([x[i] - y[i] for i in range(len(x))])
        # Hypot
        accumulator = 0
        for val in z:
            val = val * val
            accumulator = accumulator + val
        distance = math.sqrt(accumulator)
        return distance

    def viewCentroids(self):
        for points in self.centroids:
            print(*points,sep = " ")

    def run(self):
        self.llyod()

if __name__ == "__main__":
    program = clustering()
    program.run()