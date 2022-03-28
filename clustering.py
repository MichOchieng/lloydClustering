import re
import sys

class clustering:

    K:           int
    clusterSize: int

    clusters = []

    def __init__(self) -> None:
        self.getData()

    def getData(self):
        try:
            with open(sys.argv[1], mode = 'r', encoding = 'utf-8') as file:
                lines = file.readlines()
        except IndexError:
            print("Oops! You forgot to input a file name!")
        except FileNotFoundError:
            print("Error opening file " + sys.argv[1])

    def run(self):
        pass

if __name__ == "__main__":
    program = clustering()
    program.run()