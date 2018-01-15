from flask import Flask, render_template, request, Response
from game import Game
import json

app = Flask(__name__)

game = None

@app.route('/')
def run():
    global game


    action = request.args.get('action')
    position = request.args.get('position')
    if position:
        position = int(position)

    if action == 'newGame':
        game = Game()
    elif action == 'makePlayerMove':
        game.make_player_move(position)
    elif action == 'makeMenaceMove':
        game.make_menace_move(position)

    payload = game.get_status()
    print payload
    return render_template('menace.html', payload=payload)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)



