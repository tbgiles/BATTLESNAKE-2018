from ASTARBASIC import AStar
import sys
import math

tristansmaze = [[0,1,1,0,1,1],
                [1,1,1,0,1,1],
                [0,1,1,1,1,1]]

class save_daddy_plz(AStar):

    #NOTE each node is an (x,y) tuple that represents a reachable position

    def __init__(self, maze, width, height):
        self.lines = maze
        self.width = width
        self.height = height

    #NOTE Euclidian distance
    def heuristic_cost_estimate(self, n1, n2):
        (x1, y1) = n1
        (x2, y2) = n2
        return math.hypot(x2 - x1, y2 - y1)

    #NOTE Squares are all 1 unit apart
    def distance_between(self, n1, n2):
        return 1

    #NOTE returns the nodes surrounding the snake head that are traversable
    def neighbors(self, node):
        (x, y) = node #changed from x, y
        return[(nx, ny) for nx, ny in[(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]if 0 <= nx < self.width and 0 <= ny < self.height and self.lines[ny][nx] == 1]

def dont(grid, startPoint, endPoint, width, height):
    return list(save_daddy_plz(grid, width, height).astar(startPoint, endPoint))

#start = (0,1)  # we choose to start at the upper left corner
#goal = (5,0)  # we want to reach the lower right corner

# let's solve it
#foundPath = list(save_daddy_plz(tristansmaze).astar(start, goal))
#print(foundPath)
