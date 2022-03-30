import re
import sys

class clustering:

    K: int
    M: int

    clusters  = []
    centroid0 = []

    def __init__(self) -> None:
        self.getData()

    def getData(self):
        try:
            with open(sys.argv[1], mode = 'r', encoding = 'utf-8') as file:
                lines   = file.readlines()
                self.K  = lines[0][0]
                self.M  = lines[0][2]
                self.centroid0 = list(map(float,lines[1].split()))
        except IndexError:
            print("Oops! You forgot to input a file name!")
        except FileNotFoundError:
            print("Error opening file " + sys.argv[1])

    def run(self):
        pass

if __name__ == "__main__":
    program = clustering()
    program.run()