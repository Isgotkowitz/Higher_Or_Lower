"""
Modified version of the drinking card game Higher Or Lower
"""
import random as rand
import numpy as np

class HOLgame():
    """ Object representation of deck of cards being played with """
    def __init__(self, valueRange, numSuits):
        self.valueRange = valueRange
        self.numSuits = numSuits
        self.cardsInDeck = (numSuits * valueRange)
        self.reValues = np.arange(valueRange)
        self.deck = np.arange(valueRange)
        self.deck.fill(numSuits)
        self.board = np.zeros(valueRange)

    def drawCard(self):
        # Draws a random card and removes it from the deck
        randInt = rand.randint(0, len(self.reValues) - 1)
        card = self.reValues[randInt]
        if self.reValues.size == 1:
            self.deck[self.reValues[0]]
            self.deck[card] = 0
        elif self.deck[card] > 1:
            self.deck[card] -= 1
        else:
            self.deck[card] = 0
            self.reValues = np.delete(self.reValues, randInt)
        self.cardsInDeck -= 1
        return card

    def firstGuess(self, guess):
        self.topCard = self.drawCard()
        # Takes in first guess from the player
        if guess == self.topCard:
            self.board[self.topCard] += 1
            return -5
        elif guess > self.topCard:
            return 0
        else:
            return 1

    def secondGuess(self, guess):
        # Takes in second guess from the player
        if guess == self.topCard:
            self.board[self.topCard] += 1
            return guess, -3
        else:
            points = abs(self.topCard - guess)
            TC = self.topCard
            self.board[self.topCard] += 1
            return TC, points
