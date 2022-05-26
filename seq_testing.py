"""
Provides the main file from which testing is run
"""
import numpy as np

from game_modes import *
from timeit import default_timer as timer

NUM_GAMES = 2000    # Number of games each algorithm is tested over
NUM_SUITS = 4       # Number of suits each game is played with
VAL_RANGE = 13      # Defines the value range over which each game is played

timed = 1           # Turn on to measure time tests take

"""
Finds the mean, median, and standard deviation of a NumPy array and return them
in a list, in that order
"""
def get_data(arr):
    data = []
    data.append(np.mean(arr))
    data.append(np.median(arr))
    data.append(np.std(arr))
    return data

"""
Prints mean, median, and standard deviation to standard output
"""
def print_data(data):
    print("Mean = {:.5f}".format(data[0]))
    print("Median = {:.0f}".format(data[1]))
    print("Standard deviation = {:.5f}\n".format(data[2]))

def main():
    print("\nOver {} games played sequentially with {} suits and max value of {}:\n".format(NUM_GAMES, NUM_SUITS, VAL_RANGE))

    # Test simple binary seerch algorithm
    bs_points = np.zeros(NUM_GAMES)
    if timed: bs_start = timer()
    for i in range(NUM_GAMES):
        bs_points[i] = binarySearch(NUM_SUITS, VAL_RANGE)
    if timed: bs_end = timer()
    bs_data = get_data(bs_points)
    print("Simple binary search results:")
    print_data(bs_data)
    if timed: print("time elapsed for testing: {:.8f} seconds\n".format(bs_end - bs_start))

    # Test optimal algorithm
    opt_points = np.zeros(NUM_GAMES)
    if timed: opt_start = timer()
    for i in range(NUM_GAMES):
        opt_points[i] = Opt(NUM_SUITS, VAL_RANGE)
    if timed: opt_end = timer()
    opt_data = get_data(opt_points)
    print("Optimal algorithm results:")
    print_data(opt_data)
    if timed: print("time elapsed for testing: {:.8f} seconds\n".format(opt_end - opt_start))

if __name__ == "__main__":
    main()
