"""
Provides the main file from which testing is run
"""
from game_modes import *
import numpy as np

def main():
    numGames = 20000
    print("\nOver {} games:\n".format(numGames))

    # Test simple binary seerch algorithm
    points = np.zeros(numGames)
    for i in range(numGames):
        points[i] = binarySearch(4, 13)
    mean = np.mean(points)
    median = np.median(points)
    stddev = np.std(points)
    print("Simple binary search results:")
    print("Mean = {}".format(mean))
    print("Median = {}".format(median))
    print("Standard deviation = {}\n".format(stddev))

    # Test optimal algorithm
    points = np.zeros(numGames)
    for i in range(numGames):
        points[i] = Opt(4, 13)
    mean = np.mean(points)
    median = np.median(points)
    stddev = np.std(points)
    print("Optimal algorithm results:")
    print("Mean = {}".format(mean))
    print("Median = {}".format(median))
    print("Standard deviation = {}\n".format(stddev))

if __name__ == "__main__":
    main()
