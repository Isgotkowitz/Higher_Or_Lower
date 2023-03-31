"""
Driver methods for a modified version of the drinking card game Higher Or Lower
"""
import random as rand
import math
import numpy as np
from game import *

def interactiveGamePlay():
        print("Welcome to the interactive game play mode of Fuck the Dealer")
        numSuits = input("Please enter the desired number of suits (4 is standard, minimum is 1)\n")
        if numSuits == "":
            numSuits = 4
        else:
            while not (numSuits.isdigit() and int(numSuits) > 0):
                numSuits = input("Please enter a positive integer\n")
        valueRange = input("Please enter the desired max value (13 is standard, minimum is 5)\n")
        if valueRange == "":
            valueRange = 13
        else:
            while not (valueRange.isdigit() and int(valueRange) > 4):
                valueRange = input("Please enter a positive integer greater than 4\n")

        numSuits = int(numSuits)
        valueRange = int(valueRange)
        game = HOLgame(valueRange, numSuits)

        print("Value range: 1 to {}, Number of suits: {}".format(valueRange, numSuits))
        # print("Deck: ", game.deck)
        points = 0
        while game.cardsInDeck > 0:
            print("Board: ", game.board)
            print("Deck: ", game.deck)
            print("reValues ", game.reValues)
            firstGuess = input("First Guess: ")
            while not (firstGuess.isdigit() and int(firstGuess) >= 1 and int(firstGuess) <= valueRange):
                firstGuess = input("Whoops please enter a positive integer in the range 1 to max value\n")
            firstGuess = int(firstGuess) - 1
            firstAnswer = game.firstGuess(firstGuess)
            if firstAnswer == 0:
                print("Lower")
            elif firstAnswer == -5:
                print("Correct\n")
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
                print("Correct\n")
                points -= 3
            else:
                print("Incorrect, it was a", value + 1, "\n")
                points += secondAnswer
        print("Deck: ", game.deck)
        print("Board: ", game.board)
        print("Finished with {} points.".format(points))



def binarySearchPrint():
    """
    This method implements a vary naive algorithm for playing the game based on
    the Binary Search algorithm. It picks the (ceiling function of (n/2)) index of
    the array containing the elements corresponding to the value, yada yada yada
    """
    print("Welcome to the binary search algorithm for Higher Or Lower")
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
    game = HOLgame(valueRange, numSuits)

    print("Value range: 1 to {}, Number of suits: {}".format(valueRange, numSuits))

    points = 0
    while game.cardsInDeck > 0:
        print("deck:", game.deck)
        print("reValues:", game.reValues)
        print("board:", game.board)
        reValues = game.reValues
        # First guess portion
        print("reValues.size:", reValues.size, " game.reValues.size:", game.reValues.size)
        firstGuess = reValues[math.floor(reValues.size * (1/2))]
        print("first guess:", firstGuess)
        # firstGuess = game.reValues[math.floor(game.reValues.size / 2)]
        firstAnswer = game.firstGuess(firstGuess)
        if firstAnswer == -5:
            points -= 5
            print("Correct")
        # Second guess portion
        else:
            if firstAnswer == 0:
                print("Lower")
                secondGuess = reValues[math.floor(reValues.size * (1/4))]
            else:
                print("Higher")
                secondGuess = reValues[math.floor(reValues.size * (3/4))]
            value, secondAnswer = game.secondGuess(secondGuess)
            print("second guess:", secondGuess)
            if value == secondGuess:
                print("Correct")
            else:
                print("Incorrect, value:", value)
            points += secondAnswer
        print("\n")
    print("Total points:", points)

def binarySearch(numSuits, valueRange):
    """
    This method implements a vary naive algorithm for playing the game based on
    the Binary Search algorithm. It picks the (ceiling function of (n/2)) index of
    the array containing the elements corresponding to the value, yada yada yada.
    This version is intended to be used multiple times to find averages and other
    statistics
    """
    game = HOLgame(valueRange, numSuits)

    points = 0
    while game.cardsInDeck > 0:
        reValues = game.reValues
        # First guess portion
        firstGuess = reValues[math.floor(reValues.size * (1/2))] + 1
        firstAnswer = game.firstGuess(firstGuess)
        if firstAnswer == -5:
            points -= 5
        # Second guess portion
        else:
            if firstAnswer == 0:
                secondGuess = reValues[math.floor(reValues.size * (1/4))] + 1
            else:
                secondGuess = reValues[math.floor(reValues.size * (3/4))] + 1
            value, secondAnswer = game.secondGuess(secondGuess)
            points += secondAnswer
    return points

def OptPrint():
    """
    Function that makes guess with lowest expected points on every guess
    """
    print("Welcome to the optimal algorithm for Higher Or Lower")
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
    game = HOLgame(valueRange, numSuits)

    print("Value range: 1 to {}, Number of suits: {}\n".format(valueRange, numSuits))

    points = 0
    while game.cardsInDeck > 0:
        # print("deck:", game.deck)
        print("reValues:", game.reValues)
        print("board:", game.board)
        # Generate optimal first guess
        points_matrix = np.zeros((game.reValues.size, game.reValues.size))
        for i in range(game.reValues.size):
            for j in range(game.reValues.size):
                if i == j:
                    points_matrix[i][j] = -5
                else:
                    points_matrix[i][j] = abs(game.reValues[i] - game.reValues[j])
        prob_vector = np.zeros(game.reValues.size)
        print("deck:", game.deck);
        # print("prob vector:", prob_vector);
        # print("reValues:", game.reValues);
        j = 0
        for i in range(game.deck.size):
            if game.deck[i] != 0:
                # print("i, j:", i, j)
                prob_vector[j] = game.deck[i]
                j += 1
        ex_points_matrix = points_matrix@prob_vector
        print("points matrix:\n", points_matrix)
        print("prob vector:", prob_vector)
        print("expected points:", ex_points_matrix)
        firstGuess = game.reValues[0]
        firstGuessInd = 0
        for i in range(0, len(ex_points_matrix)):
            # print(game.reValues[i], i, ex_points_matrix[i], ex_points_matrix[firstGuess])
            if ex_points_matrix[i] < ex_points_matrix[firstGuessInd]:
                firstGuess = game.reValues[i]
                firstGuessInd = i
        # firstGuess += 1
        print("first guess:", firstGuess, "first guess index:", firstGuessInd);
        # print("reValues:", game.reValues);
        firstAnswer = game.firstGuess(firstGuess)
        # print("reValues:", game.reValues);
        # Generate optimal second guess
        if firstAnswer == -5:
            points -= 5
            print("Correct")
        else:
            if firstAnswer == 0:
                print("Lower")
                secondGuess = game.reValues[0]
                secondGuessInd = 0
                print("SG range", 0, "to", firstGuessInd - 1)
                for i in range(0, firstGuessInd - 1):
                    if ex_points_matrix[i] <= ex_points_matrix[secondGuessInd]:
                        secondGuess = game.reValues[i]
                        secondGuessInd = i
                # secondGuess += 1
            else:
                print("Higher")
                print("reValues length:", len(game.reValues));
                secondGuess = game.reValues[firstGuessInd + 1]
                secondGuessInd = 0
                print("SG range", firstGuessInd + 1, "to", len(ex_points_matrix) - 1)
                for i in range(firstGuessInd + 1, len(ex_points_matrix) - 1):
                    if ex_points_matrix[i] <= ex_points_matrix[secondGuessInd]:
                        secondGuess = game.reValues[i]
                        secondGuessInd = i
                # secondGuess += 1
            value, secondAnswer = game.secondGuess(secondGuess)
            print("second guess:", secondGuess)
            if value == secondGuess:
                print("Correct")
            else:
                print("value:", value)
            points += secondAnswer
        print("\n")
    print("Total points:", points)

def Opt(numSuits, valueRange):
    """
    Function that makes guess with lowest expected points on every guess
    """
    game = HOLgame(valueRange, numSuits)

    points = 0
    while game.cardsInDeck > 0:
        # Generate optimal first guess
        points_matrix = np.zeros((game.reValues.size, game.reValues.size))
        for i in range(game.reValues.size):
            for j in range(game.reValues.size):
                if i == j:
                    points_matrix[i][j] = -5
                else:
                    points_matrix[i][j] = abs(game.reValues[i] - game.reValues[j])
        prob_vector = np.zeros(game.reValues.size)
        j = 0
        for i in range(game.deck.size):
            # print(i)
            if game.deck[i] != 0:
                prob_vector[j] = game.deck[i]
                j += 1
        ex_points_matrix = points_matrix@prob_vector
        firstGuess = game.reValues[0]
        firstGuessInd = 0
        for i in range(0, len(ex_points_matrix)):
            # print(game.reValues[i], i, ex_points_matrix[i], ex_points_matrix[firstGuess])
            if ex_points_matrix[i] < ex_points_matrix[firstGuessInd]:
                firstGuess = game.reValues[i]
                firstGuessInd = i
        # firstGuess += 1
        firstAnswer = game.firstGuess(firstGuess)
        # Generate optimal second guess
        if firstAnswer == -5:
            points -= 5
        else:
            if firstAnswer == 0:
                secondGuess = game.reValues[0]
                secondGuessInd = 0
                for i in range(0, firstGuessInd - 1):
                    if ex_points_matrix[i] < ex_points_matrix[secondGuessInd]:
                        secondGuess = game.reValues[i]
                        secondGuessInd = i
                # secondGuess += 1
            else:
                secondGuess = game.reValues[0]
                secondGuessInd = 0
                for i in range(firstGuessInd + 1, len(ex_points_matrix)):
                    if ex_points_matrix[i] < ex_points_matrix[secondGuessInd]:
                        secondGuess = game.reValues[i]
                        secondGuessInd = i
                # secondGuess += 1
            value, secondAnswer = game.secondGuess(secondGuess)
            points += secondAnswer
    return points;

"""
def Opt(numSuits, valueRange):
    """
    #Function that makes guess with lowest expected points on every guess
"""
    game = HOLgame(valueRange, numSuits)

    first_points_matrix = np.zeros((game.reValues.size, game.reValues.size))
    for i in range(game.reValues.size):
        for j in range(game.reValues.size):
            if i == j:
                first_points_matrix[i][j] = -5
            else:
                first_points_matrix[i][j] = abs(game.reValues[i] - game.reValues[j])
    second_points_matrix = np.zeros((game.reValues.size, game.reValues.size))
    for i in range(game.reValues.size):
        for j in range(game.reValues.size):
            if i == j:
                second_points_matrix[i][j] = -3
            else:
                second_points_matrix[i][j] = abs(game.reValues[i] - game.reValues[j])
    prob_vector = np.zeros(game.reValues.size)
    j = 0
    for i in range(game.deck.size):
        # print(i)
        if game.deck[i] != 0:
            prob_vector[j] = game.deck[i]
            j += 1
    # ex_points_matrix = points_matrix@prob_vector

    points = 0
    while game.cardsInDeck > 0:
        # # Generate optimal first guess
        # points_matrix = np.zeros((game.reValues.size, game.reValues.size))
        # for i in range(game.reValues.size):
        #     for j in range(game.reValues.size):
        #         if i == j:
        #             points_matrix[i][j] = -5
        #         else:
        #             points_matrix[i][j] = abs(game.reValues[i] - game.reValues[j])
        # prob_vector = np.zeros(game.reValues.size)
        # j = 0
        # for i in range(game.deck.size):
        #     # print(i)
        #     if game.deck[i] != 0:
        #         prob_vector[j] = game.deck[i]
        #         j += 1
        # ex_points_matrix = points_matrix@prob_vector
        # Generate optimal first guess
        first_ex_points_matrix = np.delete(first_points_matrix@prob_vector, np.where(first_points_matrix@prob_vector == 0))
        firstGuess = game.reValues[0]
        firstGuessInd = 0
        for i in range(0, len(ex_points_matrix)):
            if first_ex_points_matrix[i] < first_ex_points_matrix[firstGuessInd]:
                firstGuess = game.reValues[i]
                firstGuessInd = i
        firstAnswer = game.firstGuess(firstGuess + 1)
        # Generate optimal second guess
        if firstAnswer == -5:
            points -= 5
            # adjust points matrices
            prob_vector[firstGuessInd] -= 1
        else:
            if firstAnswer == 0:
                second_prob_vector = np.deepcopy(prob_vector)
                second_ex_points_matrix =
                secondGuess = game.reValues[0]
                secondGuessInd = 0
                for i in range(0, firstGuessInd - 1):
                    if ex_points_matrix[i] < ex_points_matrix[secondGuessInd]:
                        secondGuess = game.reValues[i]
                        secondGuessInd = i
                # secondGuess += 1
            else:
                secondGuess = game.reValues[0]
                secondGuessInd = 0
                for i in range(firstGuessInd + 1, len(ex_points_matrix)):
                    if ex_points_matrix[i] < ex_points_matrix[secondGuessInd]:
                        secondGuess = game.reValues[i]
                        secondGuessInd = i
                # secondGuess += 1
            value, secondAnswer = game.secondGuess(secondGuess)
            points += secondAnswer
    return points;
"""

