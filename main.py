#THIS IS NOT MY CODE
#THIS BELONGS TO SENDWITHUS and is their BASIC AI on their Github!

from flask import Flask, request
import os
import random

app = Flask(__name__)

@app.route('/static/<path:path>')
def static(path):
    return app.static_file(path, root='static/')


@app.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    head_url = '%s://%s/static/head.png' % (
        app.request.urlparts.scheme,
        app.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#00FF00',
        'taunt': 'I PITY THE FOO'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'battlesnake-python'
    }


@bottle.post('/move')
def move():
    data = app.request.get_json

    # TODO: Do things with data, this is LIKELY where alot of the code will be done
    directions = ['up', 'down', 'left', 'right']

    return {
        'move': random.choice(directions),
        'taunt': 'I PITY THE FOO'
    }


# Expose WSGI app (so gunicorn can find it)
application = Flask(__name__)
if __name__ == '__main__':
    application.run(False, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
