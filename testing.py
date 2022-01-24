"""
Provides the main file from which testing and gameplay are run
"""
from HOL_game_modes import *

def main():
    # interactiveGamePlay()
    # binarySearch()
    numGames = 100
    totalPoints = 0
    for i in range(numGames):
        totalPoints += binarySearchNP(4, 13)
    print("average points:", totalPoints / numGames)

if __name__ == "__main__":
    main()
