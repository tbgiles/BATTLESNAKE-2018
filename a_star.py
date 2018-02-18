import graph, sys, random, queue

# DISTANCE HEURISTICS-----------------------------------------------------------

#Think city block distance...only integer movements
def manhattan(start, end):
    return abs(start[0]-end[0]) + abs(start[1]-end[1])

#As the crow flies
def euclidean(start, end):
    return (abs(start[0]-end[0])**2.0 + abs(start[1]-end[1])**2.0)**0.5

#No heuristic
def no_heuristic(start, end):
    return 0.0

heuristic_fns = {
    'manhattan': manhattan,
    'euclidean': euclidean,
    'none': no_heuristic,
    'default': manhattan
}

#HELPER FUNCTIONS --------------------------------------------------------------

# check if the tile at the position on the graph is an integer
def position_passable(game_grid, position, height, width):
    return position[0] >= 0 and position[1] >= 0 and position[0] < width and position[1] < height and game_grid[position[1]][position[0]]


# get the available neighbors of position
def get_neighbors(game_grid, position, height, width):
    (x, y) = position
    return [item for item in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if position_passable(game_grid, item, height, width)]


# reconstructs path from a came_from dict, a startpoint, and an endpoint
def reconstruct_path(came_from, start, end):
    path = []
    current = end
    while current != start:
        #print current
        path.insert(0, current)
        current = came_from[current]
    else:
        path.insert(0, start)
    return path #An array of tuples

#ALGORITHM----------------------------------------------------------------------

def a_star(game_grid, start, end, height, width, heuristic='default'):
    if heuristic not in heuristic_fns:
        heuristic = 'default'
    heuristic = heuristic_fns[heuristic]

    frontier = queue.PriorityQueue()

    frontier.put((0, start)) # aka open set
    came_from = {start:None} # doubles as the closed set
    past_dist = {start:0} # aka the past score g(x)

    while not frontier.empty():
        current = frontier.get()[1]

        # check if current node is the destination
        if current == end: # if so, return path
            return reconstruct_path(came_from, start, end)

        for neighbor in get_neighbors(game_grid, current, height, width):
            # calculate tentative overall distance
            tentative_past_dist = past_dist[current] + game_grid[neighbor[1]][neighbor[0]]
            if neighbor not in came_from or past_dist[neighbor] > tentative_past_dist:
                # insert into frontier by priority of lower overall_tentative_dist
                heuristic_dist = heuristic(neighbor, end)
                overall_tentative_dist = tentative_past_dist + heuristic_dist

                frontier.put((overall_tentative_dist, neighbor))
                past_dist[neighbor] = tentative_past_dist
                came_from[neighbor] = current
    return [] #Didnt find a reconstruct_path
