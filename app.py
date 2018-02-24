# Battlesnake 2018 Competition AI
# Written by:   Kelly Knights,
#               Duncan MacDonald,
#               Laura Kissack,
#               Liam Scott-Montcrief and
#               Tristan Giles
# Use whatever of this code you like LOL
# March 2018

from flask import Flask, request, jsonify
from datetime import datetime
import os, random, math, controller, datetime
#NOTE Controller is OUR files!

app = Flask(__name__) #App is now an instance of Flask.

@app.route("/start", methods=["POST"])
def start():
    return jsonify(
        color = "#800000",
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
    #game_grid = []
    print("START TIME -----")
    startTime = datetime.time();
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

    # Search for the coordinates of the closest food pellet
    target_food = controller.get_closest_food(grid_options[1], my_snake_head_x, my_snake_head_y)

    # Get the next move based on the pellet
    next_move = controller.get_move(grid_options, target_food, my_snake_head_x, my_snake_head_y, height, width)
    endTime = datetime.time()
    totalTime = startTime - endTime
    print("END TIME TOTAL ----- {}".format(totalTime))
    # Return the move in the JSON object
    return jsonify(
    move = next_move, #NOTE This is what controls where the snake goes!
    taunt = "You're tearing me apart, Lisa!"
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
