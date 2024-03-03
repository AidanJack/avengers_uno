from typing import List
from .cards import Card

import json

class Player:
    def __init__(self, name: str, hand: List[Card]):
        self.name = name
        self.hand = hand
    
    def getCard(self, cardID, cardColor):
        card = None
        for c in self.hand:
            if c.cardType == cardID and c.color == cardColor:
                card = c
                return card

    def removeCard(self, card):
        self.hand.remove(card)

    def getPlayerJSON(self):
        return json.dumps(self.name) + self.hand[0].getCardJSON()

    def getHandAsString(self):
        msg = f''
        for c in self.hand:
            msg += f' type: {c.cardType}, color: {c.color} &&'
        return msg
