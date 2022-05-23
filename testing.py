"""
Provides the main file from which testing is run
"""
from game_modes import *
import numpy as np

NUM_GAMES = 20000
NUM_SUITS = 4
VAL_RANGE = 13

def main():
    print("\nOver {} games played with {} suits and max value of {}:\n".format(NUM_GAMES, NUM_SUITS, VAL_RANGE))

    # Test simple binary seerch algorithm
    points = np.zeros(NUM_GAMES)
    for i in range(NUM_GAMES):
        points[i] = binarySearch(NUM_SUITS, VAL_RANGE)
    mean = np.mean(points)
    median = np.median(points)
    stddev = np.std(points)
    print("Simple binary search results:")
    print("Mean = {}".format(mean))
    print("Median = {}".format(median))
    print("Standard deviation = {}\n".format(stddev))

    # Test optimal algorithm
    points = np.zeros(NUM_GAMES)
    for i in range(NUM_GAMES):
        points[i] = Opt(NUM_SUITS, VAL_RANGE)
    mean = np.mean(points)
    median = np.median(points)
    stddev = np.std(points)
    print("Optimal algorithm results:")
    print("Mean = {}".format(mean))
    print("Median = {}".format(median))
    print("Standard deviation = {}\n".format(stddev))

if __name__ == "__main__":
    main()
