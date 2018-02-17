import a_star, graph, math, sys

def setup(food, width, height, snakes):
    grid_options = []
    #General grid setup
    for width in range(0, width + 1):
        for height in range(0, height + 1):
            #food_grid[(width, height)] = 0
            snake_grid[(width, height)] = 0
            general_grid[(width, height)] = 0

    #Food locations
    for pellet in food:
        food_grid[pellet] = 1
        general_grid[pellet] = 1

    #Snake locations:
    for snake in snakes:
        snake_grid[snake] = 1
        general_grid = 1

    grid_options[0] = snake_grid
    grid_options[1] = food_grid
    grid_options[2] = general_grid

    return grid_options

def get_my_snake_coordinates(snakes, your_id):
    for snake in snakes:
        if snake.get('id') == your_id:
            return snake.get('coords')

#NOTE returns a position tuple of closest food pellet
def get_closest_food(food_grid, head_x, head_y):
    current_minimum = 10000
    target_position = food_grid[0]
    for position in food_grid
        pellet_distance = a_star.euclidean((head_x, head_y),position)
        if pellet_distance < current_minimum:
            current_minimum = pellet_distance
            target_position = position
    return target_position

def get_move_letter(start, end):
    currX = start[0]
    currY = start[1]
    nextX = end[0]
    nextY = end[1]
    deltaX = nextX - currX
    deltaY = nextY - currY
    if deltaX > 0: return 'right'
    elif deltaY > 0: return 'up'
    elif deltaX < 0: return 'left'
    elif deltaY < 0: return 'down'
    else return 'right'


def get_move(grid_options, target, head_x, head_y):
    path = a_star.a_star(grid_options[0], (head_x, head_y), target )
    desired_next_position = path[1] #NOTE the 0'th coordinate is the current position
    return get_move_letter((head_x, head_y), target)
