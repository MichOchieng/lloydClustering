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
                for x in range(self.K+1,len(lines)):
                    self.data.append(
                            list(
                                map(
                                    float,lines[x].split()
                                    )
                                )
                            )
                print(self.centroids)
        except IndexError:
            print("Oops! You forgot to input a file name!")
        except FileNotFoundError:
            print("Error opening file " + sys.argv[1])

    def llyod(self):
        '''
        Centriods to clusters
        - Assign each data point to a centroid based on shortest distance
            - can use distionaries for assignment with centroid as the key
                - Convert arr val into a string

        Clusters to centroid
        - Compute new centroids from the points in their cluster
            - Find the median

        if centroids aren't the same run it back
        '''
        # Centroid to cluster
        clusters = {}
        test = []
        self.getDistance(self.centroids[0],self.data[0])

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

        


    def run(self):
        self.llyod()

if __name__ == "__main__":
    program = clustering()
    program.run()