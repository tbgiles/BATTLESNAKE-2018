from flask import Flask, request, jsonify
from datetime import datetime
import os, random

app = Flask(__name__)

@app.route("/start", methods=["POST"])
def start():
    #data = request.get_json()

    # TODO get request params
    return jsonify(
        name = "Tristan's Snake",
        color = "#FF0000",
        secondary_color = "#00FF00",
        head_url = "http://2.bp.blogspot.com/_qAms05FxvSw/TRy3kgEBjWI/AAAAAAAAAYY/xdK5e6w_P4s/s1600/The%2BRoom%2Bwe%2Bare%2Bexpecting%2521%2B.jpg",
        taunt = "Why, Lisa, why, WHY?!"
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
