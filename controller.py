import astarobject, math, sys

def grid_setup(food, width, height, snakes):

    generic_grid = []
    #General grid setup
    for y in range(0, height):
        new_list = []
        for x in range(0, width):
            new_list.append(1)
        generic_grid.append(new_list)

    food_grid = []
    #Food locations
    for [x, y] in food:
        food_grid.append([x,y])

    #Snake locations:
    for snake in snakes:
        current_snake_coordinates = snake.get('coords')
        for [x, y] in current_snake_coordinates:
            generic_grid[y][x] = 0

    grid_options = []

    grid_options.append(generic_grid)
    grid_options.append(food_grid)

    '''print('')
    for y in range(0, width):
        print('')
        for x in range(0, height):
            if snake_grid[y][x] == 0:
                print('X', end='')
            else:
                print('0', end='')'''

    return grid_options

def get_crows_dist(me, you):
    (x1, y1) = me
    (x2, y2) = you
    return abs(math.hypot(x2 - x1, y2 - y1))

def get_my_snake_coordinates(snakes, your_id):
    for snake in snakes:
        if snake.get('id') == your_id:
            return snake.get('coords')

#NOTE returns a position tuple of closest food pellet
def get_closest_food(food_list, head_x, head_y):
    current_minimum = 10000
    for position in food_list:
        pellet_distance = get_crows_dist((head_x, head_y),position)
        if pellet_distance < current_minimum:
            current_minimum = pellet_distance
            target_position = position
    return tuple(target_position)

def get_move_letter(start, end):
    currX = start[0]
    currY = start[1]
    nextX = end[0]
    nextY = end[1]
    deltaX = nextX - currX
    deltaY = nextY - currY

    '''print('dx')
    print(deltaX)
    print('dy')
    print(deltaY)'''

    if deltaX > 0:
        return 'right'
    elif deltaY > 0:
        return 'down'
    elif deltaX < 0:
        return 'left'
    elif deltaY < 0:
        return 'up'


def get_move(grid_options, target, head_x, head_y, height, width):
    path = astarobject.compute(grid_options[0], (head_x, head_y), target, width, height)
    if path:
        path = list(path)
    else:
        return random(astarobject.neighbors((head_x, head_y)));
        #return 'up' #TODO what do we do if there's no path?

    desired_next_position = path[1] #NOTE the 0'th coordinate is the current position
    return get_move_letter((head_x, head_y), desired_next_position)
