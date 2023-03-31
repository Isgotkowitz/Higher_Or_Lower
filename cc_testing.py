"""
Tests different algorithms for Higher Or Lower while utilizing principles of
currency to make testing more efficient
"""
import numpy as np
import os
import math as m
import multiprocessing as mp

from game_modes import *
from multiprocessing import Process, Queue, Lock
from timeit import default_timer as timer

N_CORES = os.cpu_count        # Max number of processes/threads that run at a time

NUM_GAMES = 2000    # Number of games each algorithm is tested over
NUM_SUITS = 4       # Number of suits each game is played with
VAL_RANGE = 13      # Defines the value range over which each game is played

dbg1 = 0
dbg2 = 0
timed = 1           # Turn on to measure time elapsed while testing

"""
Takes a function which corresponds to the algorithm that is being tested, and a
lock and a queue which are shared by all child processes to record data. All
child processes created have this function as their target
"""
def player(g_lock, g_queue, func, n_games):
    if dbg1: pid = os.getpid()
    for i in range(n_games):
        points = func(NUM_SUITS, VAL_RANGE)
        try:
            if dbg1: print("player {}!".format(pid))
            g_lock.acquire()
            if dbg1: print("lock aquired by {}!".format(pid))
            g_queue.put(points)
            # if debug: print("{}'s points: {}".format(pid, points))
        finally:
            g_lock.release()
            if dbg1: print("lock released by {}!".format(pid))

"""
Takes in a function and manages the process pool as well as aggrating the
data produced by all processes into a single list which is then returned after
NUM_GAMES have been played
"""
def pooler(func):
# def proc_manager(func):
    g_lock = Lock()
    g_queue = Queue()
    g_queue_list = []
    for i in range(N_CORES):
        p = Process(target=player, args=(g_lock, g_queue, func, m.floor(NUM_GAMES / N_CORES)))
        p.start()
        # p.join()
    while len(mp.active_children()) > 0:
        try:
            g_lock.acquire()
            while not g_queue.empty():
                g_queue_list.append(g_queue.get())
        finally:
            g_lock.release()

    if NUM_GAMES % N_CORES > 0:
        for i in range(NUM_GAMES % N_CORES):
            p = Process(target=player, args=(g_lock, g_queue, func, 1))
            p.start()
        if dbg1: print(2)
        # p.join()
        while len(mp.active_children()) > 0:
            try:
                g_lock.acquire()
                while not g_queue.empty():
                    g_queue_list.append(g_queue.get())
            finally:
                g_lock.release()
    # p.join()
    if dbg2: print("points list length: {}".format(len(g_queue_list)))
    points = np.array(g_queue_list)
    return points

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

if __name__ == '__main__':
    print("\nOver {} games played concurrently with {} suits and max value of {}:\n".format(NUM_GAMES, NUM_SUITS, VAL_RANGE))

    if dbg2: print("# cpus: {}\n".format(mp.cpu_count()))

    # Test simple binary search algorithm
    if timed: bs_start = timer()
    bs_points = pooler(binarySearch)
    if timed: bs_end = timer()
    bs_data = get_data(bs_points)
    print("Simple binary search results:")
    print_data(bs_data)
    if timed: print("time elapsed for testing: {:.8f} seconds\n".format(bs_end - bs_start))

    # Test optimal algorithm
    if timed: opt_start = timer()
    opt_points = pooler(Opt)
    if timed: opt_end = timer()
    opt_data = get_data(opt_points)
    print("Optimal algorithm results:")
    print_data(opt_data)
    if timed: print("time elapsed for testing: {:.8f} seconds\n".format(opt_end - opt_start))
