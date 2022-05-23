"""
Tests different algorithms for Higher Or Lower while utilizing principles of
currency to make testing for efficient
"""
import numpy as np
import os
import math as m

from game_modes import *
from multiprocessing import Process, Queue, Lock

N_CORES = 6 # Max number of threads that run at a time

NUM_GAMES = 600
NUM_SUITS = 4
VAL_RANGE = 13

# g_lock = Lock()
# g_queue = Queue()

# debug = 0
dbg = 1

def bs_player(g_lock, g_queue):
    pid = os.getpid()
    # print("proc {} started".format(pid))
    points = binarySearch(NUM_SUITS, VAL_RANGE)
    # g_lock.acquire()
    try:
        # print("player!")
        if dbg: print("player {}!".format(pid))
        g_lock.acquire()
        if dbg: print("lock aquired by {}!".format(pid))
        g_queue.put(points)
        # if debug: print("{}'s points: {}".format(pid, points))
    finally:
        g_lock.release()
        if dbg: print("lock released by {}!".format(pid))
    # if debug: print("proc {} joining".format(pid))

if __name__ == '__main__':
    print("\nOver {} games played with {} suits and max value of {}:\n".format(NUM_GAMES, NUM_SUITS, VAL_RANGE))

    # Test simple binary seerch algorithm
    # pool_lock = Lock()
    # points_q = Queue()
    # p = Pool(processes=5)
    # with p:
    #     results = p.map(bs_player(), range(5))
    #     print(list(results))
    # p.close()
    l = Lock()
    g_queue = Queue()
    for i in range(m.floor(NUM_GAMES / N_CORES)):
        for i in range(N_CORES):
            p = Process(target=bs_player, args=(l, g_queue,))
            p.start()
        # if dbg: print(1)
        p.join()
        if dbg: print(1)
    for i in range(NUM_GAMES % N_CORES):
        p = Process(target=bs_player, args=(l, g_queue,))
        p.start()
    # if dbg: print(2)
    p.join()
    if dbg: print(2)

    # while not g_queue.empty():
    #     print(g_queue.get())

    # points = np.zeros(NUM_GAMES)
    # for i in range(NUM_GAMES):
    #     points[i] = binarySearch(NUM_SUITS, VAL_RANGE)

    g_queue_list = []
    while not g_queue.empty():
        g_queue_list.append(g_queue.get())
    points = np.array(g_queue_list)
    # points = np.zeros(NUM_GAMES)
    mean = np.mean(points)
    median = np.median(points)
    stddev = np.std(points)
    print("Simple binary search results:")
    print("Mean = {}".format(mean))
    print("Median = {}".format(median))
    print("Standard deviation = {}\n".format(stddev))

    # Test optimal algorithm
    # points = np.zeros(NUM_GAMES)
    # for i in range(NUM_GAMES):
    #     points[i] = Opt(NUM_SUITS, VAL_RANGE);
    # mean = np.mean(points)
    # median = np.median(points)
    # stddev = np.std(points)
    # print("Optimal algorithm results:")
    # print("Mean = {}".format(mean))
    # print("Median = {}".format(median))
    # print("Standard deviation = {}\n".format(stddev))
