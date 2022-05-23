"""
Provides the main file from which testing is run
"""
from game_modes import *
import numpy as np

def main():
    numGames = 20000
    points = np.zeros(numGames)
    for i in range(numGames):
        points[i] = binarySearchNP(1, 20)
    mean = np.mean(points)
    median = np.median(points)
    stddev = np.std(points)
    print("\nOver {} games:".format(numGames))
    print("Mean = {}".format(mean))
    print("Median = {}".format(median))
    print("Standard deviation = {}\n".format(stddev))

if __name__ == "__main__":
    main()
