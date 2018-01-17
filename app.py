# Battlesnake 2018 Competition AI
# Written by Tristan Giles - 2018

from flask import Flask, request, jsonify
from datetime import datetime
import os, random, math

app = Flask(__name__) #App is now an instance of Flask.

def get_move_letters(x, y, my_snake_x, my_snake_y):
    disp_x = x - my_snake_x
    disp_y = y - my_snake_y

    if abs(disp_x) > abs(disp_y):
        if disp_x < 0:
            return "left"
        else:
            return "right"
    else:
        if disp_y < 0:
            return "down"
        else:
            return "up"

def get_next_move(food, height, width, snakes, dead_snake, my_snake_x, my_snake_y):
    min_dist = width + height
    min_x = 0
    min_y = 0
    for pellet in food:
        x = pellet[0]
        y = pellet[1]
        dist = math.sqrt((x-my_snake_x)**2 + (y-my_snake_y)**2)
        if dist <= min_dist:
            min_dist = dist
            min_x = x
            min_y = y
    return get_move_letters(min_x, min_y, my_snake_x, my_snake_y)

@app.route("/start", methods=["POST"])
def start():
    data = request.get_json()
    game_id = data.get("game_id")
    height = data.get("height")
    width = data.get("width")

    height += 30

    # TODO get request params
    return jsonify(
        color = "#FFFFFF",
        name = "Tommy Wiseau",
        head_url = "http://2.bp.blogspot.com/_qAms05FxvSw/TRy3kgEBjWI/AAAAAAAAAYY/xdK5e6w_P4s/s1600/The%2BRoom%2Bwe%2Bare%2Bexpecting%2521%2B.jpg",
        # The below fields are NOT REQUIRED
        taunt = "Why, Lisa, why, WHY?!",
        head_type = "sand-worm",
        tail_type = "pixel",
        secondary_color = "#000000",
    )

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    food = data.get("food") #Array
    game_id = data.get("game_id")
    height = data.get("height")
    snakes = data.get("snakes") #Array
    dead_snake = data.get("dead_snake") #array
    turn = data.get("turn")
    width = data.get("width")
    you = data.get("you")

    for snake in snakes:
        if snake.get("id") == you:
            my_snake_x = snake.get("coords")[0][0]
            my_snake_y = snake.get("coords")[0][1]

    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']

    return jsonify(
    move = get_next_move(food, height, width, snakes, dead_snake, my_snake_x, my_snake_y),
    taunt = "You're tearing me apart, Lisa!"
    )

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
