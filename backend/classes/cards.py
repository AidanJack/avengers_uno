import json

class Card:
    def __init__(self, cardType: int, color: str):
        self.cardType = cardType
        self.color = color

    def applyEffect(self, turnPhase, activePlayerIndex, direction, activePlayer, generateCards):
        pass

    def getCardJSON(self):
        return json.dumps(self.__dict__)

class NumberCard(Card):
    def __init__(self, cardType: int, color: str):
        super().__init__(cardType, color)

    # No Effect
    def applyEffect(self, turnPhase, activePlayerIndex, direction, activePlayer, generateCards):
        pass

class Skip(Card):
    def __init__(self, cardType: int, color: str):
        super().__init__(cardType, color)

    # Increments Active Player by Two
    def applyEffect(self, turnPhase, activePlayerIndex, direction, activePlayer, generateCards):
        if turnPhase == 1:    
            activePlayerIndex += 1 * direction # This will get called after already incrementing it

class Reverse(Card):
    def __init__(self, cardType: int, color: str):
        super().__init__(cardType, color)

    # Sets direction to -1
    def applyEffect(self, turnPhase, activePlayerIndex, direction, activePlayer, generateCards):
        if turnPhase == 1:
            direction *= -1

class DrawTwo(Card):
    def __init__(self, cardType: int, color: str):
        super().__init__(cardType, color)

    # Gets two new cards, adds them to the active player 
    def applyEffect(self, turnPhase, activePlayerIndex, direction, activePlayer, generateCards):
        if turnPhase == 0:
            activePlayer.hand += generateCards(2)

class Wild(Card):
    def __init__(self, cardType: int, color: str):
        super().__init__(cardType, color)

    # Sets this card color to player choice
    def applyEffect(self, turnPhase, activePlayerIndex, direction, activePlayer, generateCards):
        if turnPhase == 1:
            self.color = "RED" #TODO: add players choice 

class WildDrawFour(Card):
    def __init__(self, cardType: int, color: str):
        super().__init__(cardType, color)

    # Gets four new cards, adds them to the active player, sets this card color to player choice
    def applyEffect(self, turnPhase, activePlayerIndex, direction, activePlayer, generateCards):
        if turnPhase == 0:
            activePlayer.hand += generateCards(4)

        elif turnPhase == 1:
            self.color = "RED" #TODO: add players choice 

    