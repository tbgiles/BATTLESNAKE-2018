# Battlesnake 2018 Competition AI
# Written by Tristan Giles - 2018

from flask import Flask, request, jsonify
from datetime import datetime
import os, random, math

app = Flask(__name__) #App is now an instance of Flask.

def get_move_letters(x, y, my_snake_x, my_snake_y, game_grid):
    disp_x = x - my_snake_x
    disp_y = y - my_snake_y

    #if abs(disp_x) > abs(disp_y):
    #if disp_x < 0 and not game_grid[[my_snake_x - 1, my_snake_y]]:
        #return "left"
    #elif not game_grid[[my_snake_x + 1, my_snake_y]] == 1:
    #    return "right"
    #elif disp_y < 0 and not game_grid[[my_snake_x, my_snake_y + 1]] == 1:
    #    return "up"
    #else:
        #return "down"

    #if abs(disp_x) > abs(disp_y):
    if disp_x < 0 and not game_grid[(my_snake_x - 1, my_snake_y)] == 1:
        return "left"
    elif not game_grid[(my_snake_x + 1, my_snake_y)] == 1:
        return "right"
    elif disp_y < 0 and not game_grid[(my_snake_x, my_snake_y + 1)] == 1:
        return "up"
    else:
        return "down"

def get_next_move(food, height, width, snakes, dead_snake, my_snake_x, my_snake_y, game_grid):
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
    return get_move_letters(min_x, min_y, my_snake_x, my_snake_y, game_grid)

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
    game_grid = {}
    data = request.get_json()
    food = data.get("food") #Array
    game_id = data.get("game_id")
    height = data.get("height")
    snakes = data.get("snakes") #Array
    dead_snake = data.get("dead_snake") #array
    turn = data.get("turn")
    width = data.get("width")
    you = data.get("you")

    for x in range(0, width + 1):
        for y in range(0, height + 1):
            game_grid[(x, y)] = 0

    for snake in snakes:
        for coordinate_pair in snake.get("coords"):
            game_grid[tuple(coordinate_pair)] = 1;
        if snake.get("id") == you:
            my_snake_x = snake.get("coords")[0][0]
            my_snake_y = snake.get("coords")[0][1]
            #TODO Maybe simplify this to a 1x2 list?

    return jsonify(
    move = get_next_move(food, height, width, snakes, dead_snake, my_snake_x, my_snake_y, game_grid), #TODO This is what controls where the snake goes!
    taunt = "You're tearing me apart, Lisa!"
    )

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
