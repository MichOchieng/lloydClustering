import sys

class clustering:

    K: int
    M: int

    clusters  = []
    centroids = []
    data      = [] 

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
                print(self.data)
        except IndexError:
            print("Oops! You forgot to input a file name!")
        except FileNotFoundError:
            print("Error opening file " + sys.argv[1])

    def llyod(self):
        pass

    def run(self):
        self.llyod()

if __name__ == "__main__":
    program = clustering()
    program.run()