from .cards import Card
from .players import Player
from queue import Queue
from typing import List

class Game:
    def __init__(self):
        self.deckSize = 72
        self.deck = self.createDeck()
        self.discard = []
        self.prevCard = None
        self.players = self.createPlayers() # Current Player will be the player at index 0
    
    def checkMoveLegality(self, card: Card):
        # Wildcards can always be played
        if card.cardType == 13 or card.cardType == 14:
            return True
        
        # If color matches prev card then legal
        if card.color == prevCard.color:
            return True

        # If cardType matches then legal
        if card.cardType == prev.cardType:
            return True
        


    def createPlayers(self):
        pass
    
    # Rough in for now. Cards will probably become subsclasses for various card types rather than having a type int
    def createDeck(self):
        deck = []

        for color in ["RED", "GREEN", "BLUE", "YELLOW"]:
            # Create Numbered Cards
            for i in range(10):
                deck.append(Card(i, color))

            # Create Action Cards
            for i in range(10, 13):
                for _ in range(2):
                    deck.append(Card(i, color))

        # Create Wildcards
        for i in range(13, 15):
            for _ in range(4):
                deck.append(Card(i, "WILD"))

        return deck
        
