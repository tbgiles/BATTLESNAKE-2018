from ASTARBASIC import AStar
import sys
import math

tristansmaze = [[0,1,1,0,1,1],
                [1,1,1,0,1,1],
                [0,1,1,1,1,1]]

class save_daddy_plz(AStar):

    """sample use of the astar algorithm. In this exemple we work on a maze made of ascii characters,
    and a 'node' is just a (x,y) tuple that represents a reachable position"""

    def __init__(self, maze, width, height):
        self.lines = maze
        self.width = width
        self.height = height

    def heuristic_cost_estimate(self, n1, n2):
        """computes the 'direct' distance between two (x,y) tuples"""
        (x1, y1) = n1
        (x2, y2) = n2
        return math.hypot(x2 - x1, y2 - y1)

    def distance_between(self, n1, n2):
        """this method always returns 1, as two 'neighbors' are always adajcent"""
        return 1

    def neighbors(self, node):
        """ for a given coordinate in the maze, returns up to 4 adjacent(north,east,south,west)
            nodes that can be reached (=any adjacent coordinate that is not a wall)
        """
        x, y = node
        return[(nx, ny) for nx, ny in[(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]if 0 <= nx < self.width and 0 <= ny < self.height and self.lines[ny][nx] == 1]

def dont(grid, startPoint, endPoint, width, height):
    print('start')
    print(startPoint)
    print('end')
    print(endPoint)
    print('grid')
    print(grid)
    return list(save_daddy_plz(grid, width, height).astar(startPoint, endPoint))
#start = (0,1)  # we choose to start at the upper left corner
#goal = (5,0)  # we want to reach the lower right corner

# let's solve it
#foundPath = list(save_daddy_plz(tristansmaze).astar(start, goal))
#print(foundPath)
