from flask import Flask
from classes.game import Game

app = Flask(__name__)

game = None # Replace with some sort of storage either database or flask sessions maybe?

@app.route('/')
def createGame():
    global game
    if game is None:
        game = Game()
    return f''

@app.route('/player/create')
def createPlayer():
    msg = f''
    if game is not None:
        msg = f'Player Added'
    else:
        msg = f'Player Could not be added'
    return msg


if __name__ == '__main__':
    app.run(debug=True, port=8080)