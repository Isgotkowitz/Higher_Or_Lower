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

    def adjustReValues(self, card):
        # Alter the reValues array to reflect the remaining values still in
        # the deck
        reValues_index = np.where(self.reValues == card);
        self.deck[card] -= 1
        if self.deck[card] == 0:
            self.reValues = np.delete(self.reValues, reValues_index)
        self.cardsInDeck -= 1
        return None

    def drawCard(self):
        # Draws a random card and removes it from the deck
        randInt = rand.randint(0, self.cardsInDeck - 1)
        for i in range(self.valueRange):
            if self.deck[i] == 0:
                continue
            randInt -= self.deck[i]
            if randInt <= 0:
                return i
        print("error: did not correctly draw card")
        return -1

    def firstGuess(self, guess):
        self.topCard = self.drawCard()
        # Takes in first guess from the player
        if guess == self.topCard:
            self.adjustReValues(self.topCard)
            self.board[self.topCard] += 1
            return -5
        elif guess > self.topCard:
            # Guess is higher
            return 0
        else:
            # Guess is lower
            return 1

    def secondGuess(self, guess):
        self.adjustReValues(self.topCard)
        # Takes in second guess from the player
        if guess == self.topCard:
            self.board[self.topCard] += 1
            return guess, -3
        else:
            points = abs(self.topCard - guess)
            TC = self.topCard
            self.board[self.topCard] += 1
            return TC, points
