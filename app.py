from flask import Flask
from flask import request
from game import Game
from flask import Response
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

    # try:
    payload = ""
    if action == 'newGame':
        game = Game()
    elif action == 'makePlayerMove':
        game.make_player_move(position)
    elif action == 'makeMenaceMove':
        game.make_menace_move(position)

    payload = json.dumps(game.get_status())
    return Response(payload, status=200, mimetype='application/json')

    # except Exception as e:
    #     return  Response(json.dumps({'err':e.message}), status=400, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)



