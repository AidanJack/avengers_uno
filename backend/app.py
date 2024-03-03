from flask import Flask
from classes.game import Game
from classes.players import Player

import json

app = Flask(__name__)

games = []

@app.route('/game/start/<player1>/<player2>')
def createGame(player1, player2):
    msg = f''
    if len(games) == 0:
        game = Game(player1, player2)  
        games.append(game)
        msg = f'Game Created'
    else:
        msg = f'Game not Created'
    return msg

@app.route('/game/play/<cardID>/<cardColor>')
def playCard(cardID, cardColor):
    msg = f''
    if len(games) != 0:
        cardID = int(cardID)
        msg = games[0].playTurn(cardID, cardColor)
    else:
        msg = f'Game not Created'
    return msg

@app.route('/game/view/hand/<playerName>')
def getPlayerHand(playerName):
    msg = f''
    if len(games) != 0:
        msg = games[0].getPlayerHand(playerName)
    else:
        msg = f'Cannot check hand, game not created.'
    return msg


if __name__ == '__main__':
    app.run(debug=True, port=8080)