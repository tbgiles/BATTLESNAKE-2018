# Battlesnake 2018 Competition AI
# Written by Tristan Giles - 2018

from flask import Flask, request, jsonify
from datetime import datetime
import os, random

app = Flask(__name__) #App is now an instance of Flask.

@app.route("/start", methods=["POST"])
def start():
    data = request.get_json()

    # TODO get request params
    return jsonify(
        color = "#FFFFFF",
        name = "Tristan's Snake",
        head_url = "http://2.bp.blogspot.com/_qAms05FxvSw/TRy3kgEBjWI/AAAAAAAAAYY/xdK5e6w_P4s/s1600/The%2BRoom%2Bwe%2Bare%2Bexpecting%2521%2B.jpg",
        taunt = "Why, Lisa, why, WHY?!",
        head_type = "sand-worm"
        tail_type = "pixel",
        secondary_color = "#000000",

        data = str(data)
    )


@app.route("/move", methods=["POST"])
def move():
    #data = request.get_json()

    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']

    return jsonify(
    move = random.choice(directions),
    taunt = "You're tearing me apart, Lisa!"
    )

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
