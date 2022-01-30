"""
Provides the main file from which testing and gameplay are run
"""
from game_modes import *

def main():
    # interactiveGamePlay()
    # binarySearch()
    numGames = 20000
    totalPoints = 0
    for i in range(numGames):
        totalPoints += binarySearchNP(1, 20)
    print("average points over {} games: {}".format(numGames, totalPoints / numGames))

if __name__ == "__main__":
    main()
