from flask import Flask, render_template, request, Response
from game import Game
import time

app = Flask(__name__)

game = None

@app.route('/')
def run():
    global game


    action = request.args.get('action')
    position = request.args.get('position')
    if position:
        position = int(position)

    if action == 'newGame' or not game:
        game = Game()

    if action == 'makePlayerMove':
        game.make_player_move(position)
    elif action == 'makeMenaceMove':
        game.make_menace_move(position)

    payload = game.get_status()
    print payload
    if payload["gameover"] != 0:
        html = render_template('menace.html', payload=payload, now=time.time(), use_modal=False)
        try:
            with open("results/results_{0}_{1}".format(game.gid, payload["gameover"]), "wb") as f:
                f.write(html)
        except Exception as e:
            print "failed writing snapshot", repr(game.gid), ":", repr(e)
    return render_template('menace.html', payload=payload, now=time.time(), use_modal=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)



