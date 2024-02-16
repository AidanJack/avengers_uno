from typing import List
from .cards import Card

class Player:
    def __init__(self, name: str, hand: List[Card]):
        self.name = name
        self.hand = hand
    
    def playCard(self, card: Card):
        pass