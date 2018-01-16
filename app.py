from flask import Flask, request, jsonify
from datetime import datetime
import os
app = Flask(__name__)

@app.route("/start", methods=["POST"])
def start():
    #data = request.get_json()
    # TODO get request params
    return jsonify(
        color="#FF0000",
        secondary_color="#00FF00",
        head_url="http://placecage.com/c/100/100"
    )


@app.route("/move", methods=["POST"])
def move():
    #data = request.get_json()

    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']

    return jsonify(
    move = random.choice(directions), taunt = "YOLO"
    )



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
