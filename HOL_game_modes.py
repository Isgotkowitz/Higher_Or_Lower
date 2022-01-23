"""
Driver for a modified version of the drinking card game Fuck the Dealer
"""
import sys
import random as rand
import math
import numpy as np
from FTDgame import *

def interactiveGamePlay():
        print("Welcome to the interactive game play mode of Fuck the Dealer")
        numSuits = input("Please enter the desired number of suits (4 is standard, minimum is 1)\n")
        if numSuits == "":
            numSuits = 4
        else:
            while not (numSuits.isdigit() and int(numSuits) > 0):
                numSuits = input("Whoops please enter a positive integer\n")
        valueRange = input("Please enter the desired max value (13 is standard, minimum is 5)\n")
        if valueRange == "":
            valueRange = 13
        else:
            while not (valueRange.isdigit() and int(valueRange) > 4):
                valueRange = input("Whoops please enter a positive integer greater than 4\n")

        numSuits = int(numSuits)
        valueRange = int(valueRange)
        game = FTDgame(valueRange, numSuits)

        print("Value range: 1 to {}, Number of suits: {}".format(valueRange, numSuits))
        # print("Deck: ", game.deck)
        points = 0
        while game.cardsInDeck > 0:
            # print("Deck: ", game.deck)
            print("Board: ", game.board)
            # print("Top card: ", (game.topCard + 1))
            firstGuess = input("First Guess: ")
            while not (firstGuess.isdigit() and int(firstGuess) >= 1 and int(firstGuess) <= valueRange):
                firstGuess = input("Whoops please enter a positive integer in the range 1 to max value\n")
            firstGuess = int(firstGuess) - 1
            firstAnswer = game.firstGuess(firstGuess)
            if firstAnswer == 0:
                print("Lower")
            elif firstAnswer == -5:
                print("Correct")
                points -= 5
                continue
            else:
                print("Higher")
            secondGuess = input("Second Guess: ")
            while not (secondGuess.isdigit() and int(secondGuess) >= 1 and int(secondGuess) <= valueRange):
                firstGuess = input("Whoops please enter a positive integer in the range 1 to max value\n")
            secondGuess = int(secondGuess) - 1
            value, secondAnswer = game.secondGuess(secondGuess)
            if secondAnswer == -3:
                print("Correct")
                points -= 3
            else:
                print("Incorrect, it was a", value + 1)
                points += secondAnswer
        print("Deck: ", game.deck)
        print("Board: ", game.board)
        print("Finished with {} points.".format(points))



def binarySearch():
    """
    This method implements a vary naive algorithm for playing the game based on
    the Binary Search algorithm. It picks the (ceiling function of (n/2)) index of
    the array containing the elements corresponding to the value, yada yada yada
    """
    print("Welcome to the binary search algorithm for Fuck the Dealer")
    numSuits = input("Please enter the desired number of suits (4 is standard, minimum is 1)\n")
    if numSuits == "":
        numSuits = 4
    else:
        while not (numSuits.isdigit() and int(numSuits) > 0):
            numSuits = input("Whoops please enter a positive integer\n")
    valueRange = input("Please enter the desired max value (13 is standard, minimum is 5)\n")
    if valueRange == "":
        valueRange = 13
    else:
        while not (valueRange.isdigit() and int(valueRange) > 4):
            valueRange = input("Whoops please enter a positive integer greater than 4\n")

    numSuits = int(numSuits)
    valueRange = int(valueRange)
    game = FTDgame(valueRange, numSuits)

    print("Value range: 1 to {}, Number of suits: {}".format(valueRange, numSuits))

    points = 0
    while game.cardsInDeck > 0:
        print("deck:", game.deck)
        print("reValues:", game.reValues)
        print("board:", game.board)
        reValues = game.reValues
        # First guess portion
        firstGuess = reValues[math.floor(reValues.size * (1/2))] + 1
        print("first guess:", firstGuess)
        # firstGuess = game.reValues[math.floor(game.reValues.size / 2)]
        firstAnswer = game.firstGuess(firstGuess)
        if firstAnswer == -5:
            points -= 5
            print("Correct")
            # continue
        # Second guess portion
        else:
            if firstAnswer == 0:
                print("Lower")
                secondGuess = reValues[math.floor(reValues.size * (1/4))] + 1
            else:
                print("Higher")
                secondGuess = reValues[math.floor(reValues.size * (3/4))] + 1
            value, secondAnswer = game.secondGuess(secondGuess)
            print("second guess:", secondGuess)
            if value == secondGuess:
                print("Correct")
            points += secondAnswer
            print("value:", value)
        print("\n")
    print("Total points:", points)

def main():
    interactiveGamePlay()
    # binarySearch()

if __name__ == "__main__":
    main()
