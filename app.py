# Battlesnake 2018 Competition AI
# Written by:   Kelly Knights,
#               Duncan MacDonald,
#               Laura Kissack,
#               Liam Scott-Montcrief and
#               Tristan Giles
# Use whatever of this code you like LOL
# March 2018

import os, random, math, controller
from flask import Flask, request, jsonify
from datetime import datetime
from timeit import default_timer as timer

height = 0
width = 0
game_id = 0

app = Flask(__name__) #App is now an instance of Flask.

@app.route("/start", methods=["POST"])
def start():
    global height
    global width
    global game_id
    data = request.get_json()
    #game_id = data.get("game_id")
    height = data.get("height")
    width = data.get("width")

    return jsonify(
        color = "#800000",
        secondary_color = "#000000",
        name = "Tommy Wiseau",
        head_url = "http://2.bp.blogspot.com/_qAms05FxvSw/TRy3kgEBjWI/AAAAAAAAAYY/xdK5e6w_P4s/s1600/The%2BRoom%2Bwe%2Bare%2Bexpecting%2521%2B.jpg",
        # The below fields are NOT REQUIRED
        taunt = "Why, Lisa, why, WHY?!",
        head_type = "sand-worm",
        tail_type = "pixel",

    )

@app.route("/move", methods=["POST"])
def move():
    #start = timer() #NOTE THIS IS OUR TIMER START POINT
    data = request.get_json()
    width = data.get("width")
    height = date.get("height")
    print('')
    print("Game height:{}, Game width:{}".format(height,width))
    food = data.get("food").get("data") #Array
    snakes = data.get("snakes").get("data") #Array
    you = data.get("you")
    print('')
    print('turn = {}'.format(data.get("turn")))
    myHealth = you.get("body").get("health")
    myLength = you.get("body").get("length")
    mySnake = you.get("body").get("data")

    #NOTE grid_options[0] = general_grid // grid_options[1] = food_grid
    grid_options = controller.grid_setup(food, width, height, snakes, mySnake)

    #NOTE Now, set our coordinates!
    mySnakeX = mySnake[0].get("x")
    mySnakeY = mySnake[0].get("y")

    #NOTE Search for the coordinates of the closest food pellet
    target_food = controller.get_closest_food(grid_options[1], mySnakeX, mySnakeY)

    #NOTE Get the next move based on the pellet
    next_move = controller.get_move(grid_options, target_food, mySnakeX, mySnakeY, height, width)

    #NOTE This is the end reference point of the timer. Just to get a good idea of what the runtime of the program is in total
    #end = timer()
    #print("RUNTIME: {0}ms. MAX 200ms, currently using {1}%".format(((end - start) * 1000),(((end - start) * 1000) / 2)))

    #NOTE Return the move in the JSON object wrapper
    return jsonify(
    move = next_move #NOTE This is what controls where the snake goes!
    )

@app.route("/end", methods=["POST"])
def end():
    return true, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
