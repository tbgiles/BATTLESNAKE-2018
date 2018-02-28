from abc import ABCMeta, abstractmethod
from heapq import heappush, heappop

infinityNum = float('inf')

class AStar:
    __metaclass__ = ABCMeta
    class SearchNode:
        #NOTE No need to waste time in RAM, we know what data needs to be accessed and saved
        __slots__ = ('data', 'gscore', 'fscore', 'closed', 'came_from', 'out_openset')

        def __init__(self, data, gscore=infinityNum, fscore=infinityNum):
            self.data = data
            self.gscore = gscore
            self.fscore = fscore
            self.closed = False
            self.out_openset = True
            self.came_from = None
            print("Init")

        #NOTE Defining what less than means with concern to the class
        def __lt__(self, b):
            return self.fscore < b.fscore

    class SearchNodeDict(dict):
        def __missing__(self, k):
            v = AStar.SearchNode(k)
            self.__setitem__(k, v)
            print("Search")
            return v

    @abstractmethod
    def heuristic_cost_estimate(self, current, goal):
        #NOTE Computes a rough distance between a node and the goal, implemented in a subclass. Second parameter is always the goal
        raise NotImplementedError

    @abstractmethod
    def distance_between(self, n1, n2):
        #NOTE gives an implemented difference between nodes. Defined in the the object file
        raise NotImplementedError

    @abstractmethod
    def neighbors(self, node):
        #NOTE For a given node, returns list of neighbours
        raise NotImplementedError

    def is_goal_reached(self, current, goal):
        #NOTE Returns true when 'current' is the goal
        return current == goal

    def reconstruct_path(self, last, reversePath=False):
        def _gen():
            current = last
            while current:
                yield current.data
                current = current.came_from
        if reversePath:
            return _gen()
        else:
            return reversed(list(_gen()))

    def astar(self, start, goal, reversePath=False):
        if self.is_goal_reached(start, goal):
            return [start]
        searchNodes = AStar.SearchNodeDict()
        startNode = searchNodes[start] = AStar.SearchNode(start, gscore=.0, fscore=self.heuristic_cost_estimate(start, goal))
        openSet = []
        heappush(openSet, startNode)
        while openSet:
            current = heappop(openSet)
            if self.is_goal_reached(current.data, goal):
                return self.reconstruct_path(current, reversePath)
            print("not goal")
            current.out_openset = True
            current.closed = True
            for neighbor in [searchNodes[n] for n in self.neighbors(current.data)]:
                if neighbor.closed:
                    continue
                tentative_gscore = current.gscore + self.distance_between(current.data, neighbor.data)
                if tentative_gscore >= neighbor.gscore:
                    continue
                neighbor.came_from = current
                neighbor.gscore = tentative_gscore
                neighbor.fscore = tentative_gscore + self.heuristic_cost_estimate(neighbor.data, goal)
                if neighbor.out_openset:
                    neighbor.out_openset = False
                    heappush(openSet, neighbor)
        return None
