from flask import Flask, request
from datetime import datetime
import os
app = Flask(__name__)

@app.route('/start', methods=['GET', 'POST'])
def start():
    data = request.get_json()
    # TODO get request params
    return {
        "color": "#FF0000",
        "secondary_color": "#00FF00",
        "head_url": "http://placecage.com/c/100/100",
        "name": "MY SNAKE",
        "taunt": "What is happening?"
        "head_type": "pixel",
        "tail_type": "pixel"
        }


@app.route('/move', methods=['GET', 'POST'])
def move():
    data = request.get_json()

    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']

    return {
        'move': random.choice(directions),
        'taunt': 'YOLO'
        }


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
