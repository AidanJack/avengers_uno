from .cards import Card, NumberCard, Skip, Reverse, DrawTwo, Wild, WildDrawFour
from .players import Player
from queue import Queue
from typing import List
import random as rng
import json

class Game:
    def __init__(self, player1, player2):

        self.STARTING_HAND_SIZE = 7
        self.deckSize = 72

        self.discard = []

        self.deck = self.createDeck()
        self.active_player = 0
        self.turnDirection = 1 # 1 or -1 direction multiplier
        self.players = self.createPlayers(player1, player2) # Current Player will be the player at index 0
        self.prevCard = self.setInitialCard()
        self.moveMade = False
        self.prevCard.applyEffect(0, self.active_player, self.turnDirection, self.players[self.active_player], self.generateCards)
        print(f'{self.prevCard.cardType} && {self.prevCard.color}')

    def checkMoveLegality(self, card: Card):
        # Wildcards can always be played
        if card.cardType >= 13:
            return True
        
        # If color matches prev card then legal
        if card.color == self.prevCard.color:
            return True

        # If cardType matches then legal
        if card.cardType == self.prevCard.cardType:
            return True
        
        return False

    def createPlayers(self, player1, player2):
        hand1 = self.generateCards(self.STARTING_HAND_SIZE)
        player1 = Player(player1, hand1)
        hand2 = self.generateCards(self.STARTING_HAND_SIZE)
        player2 = Player(player2, hand2)
        return [player1, player2]
    
    # Rough in for now. Cards will probably become subsclasses for various card types rather than having a type int
    def createDeck(self):
        deck = []

        for color in ["RED", "GREEN", "BLUE", "YELLOW"]:
            # Create Numbered Cards
            for i in range(10):
                deck.append(NumberCard(i, color))

            # Create Action Cards
            for i in range(10, 13):
                for _ in range(2):
                    match i:
                        case 10:
                            deck.append(Skip(i, color))
                        case 11:
                            deck.append(Reverse(i, color))
                        case 12:
                            deck.append(DrawTwo(i, color))                       

        # Create Wildcards
        for i in range(13, 15):
            for _ in range(4):
                match i:
                    case 13:
                        deck.append(Wild(i, "WILD"))
                    case 14:
                        deck.append(WildDrawFour(i, "WILD"))

        return deck
        
    def generateCards(self, numCards):
        hand = []
        for i in range(numCards):
            # Grab random card
            cardIndex = rng.randint(0, self.deckSize - 1)
            card = self.deck[cardIndex]

            # Remove Card and Update Deck Size
            self.deck.pop(cardIndex)
            self.deckSize -= 1

            # Append Card
            hand.append(card)
        return hand
    
    def setInitialCard(self):
        cardIndex = rng.randint(0, self.deckSize - 1)
        card = self.deck[cardIndex]

        self.deck.pop(cardIndex)
        self.deckSize -= 1

        return card

    def playTurn(self, cardID, cardColor):
        # Check and Play Move
        player = self.players[self.active_player]
        card = player.getCard(cardID, cardColor)
        print(f'card found: {card}')

        if self.checkMoveLegality(card):
            self.discard.append(card)
            self.prevCard = card
            player.removeCard(card)
        else:
            return f'Illegal Move'

        # Apply end of turn card effects
        self.prevCard.applyEffect(0, self.active_player, self.turnDirection, self.players[self.active_player], self.generateCards)

        # Change active player
        self.active_player = (self.active_player + 1 * self.turnDirection) % len(self.players)

        if self.checkWinCondition():
            pass # TODO: Trigger Game Over
        return f'Move Played'

    def getPlayerHand(self, playerName):
        for p in self.players:
            if p.name == playerName:
                return p.getHandAsString()

    def checkWinCondition(self):
        win = False
        if len(self.players[self.active_player].hand) <= 0:
            win = True
        else:
            win = False
        return win

    def NextTurn(self):
        pass

    def getGameJSON(self):
        f'replace with json'
