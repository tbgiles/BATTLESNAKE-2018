# Battlesnake 2018 Competition AI
# Written by Tristan Giles - 2018

from flask import Flask, request, jsonify
from datetime import datetime
import os, random, math
import controller

app = Flask(__name__) #App is now an instance of Flask.

@app.route("/start", methods=["POST"])
def start():
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
    game_grid = []
    data = request.get_json()
    food = data.get("food") #Array
    game_id = data.get("game_id")
    height = data.get("height")
    snakes = data.get("snakes") #Array
    dead_snake = data.get("dead_snake") #array
    turn = data.get("turn")
    width = data.get("width")
    you = data.get("you")

    #NOTE grid_options[0] = snake_grid
    #NOTE grid_options[1] = food_grid
    #NOTE grid_options[2] = general_grid
    grid_options = controller.setup(food, width, height, snakes)
    my_snake_coords = snakes[0].get('coords')
    my_snake_head_x = my_snake_coords[0][0]
    my_snake_head_y = my_snake_coords[0][1]

    print('x: {}'.format(my_snake_head_x))
    print('y: {}'.format(my_snake_head_y))

    #Search for the coordinates of the closest food pellet
    target_food = controller.get_closest_food(grid_options[1], my_snake_head_x, my_snake_head_y)

    #Get the next move based on the pellet
    next_move = controller.get_move(grid_options, target_food, my_snake_head_x, my_snake_head_y, height, width)



    return jsonify(
    move = next_move,   #next_move, #TODO This is what controls where the snake goes!
    taunt = "width:{} height:{}".format(width,height)#"You're tearing me apart, Lisa!"
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
