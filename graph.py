class graph():
    def __init__(self):
        # graph is stored as vertex:{neighbors:weight} pairs
        # eg. {foo: {bar:2, baz:1}, bar:{foo:2, baz:4}, baz:{foo:1,bar:4}}
        self.neighbors = {}

    # add vertex
    def add_vertex(self, vertex):
        # add vertex only if not already in graph
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    # adds edge between v1 and v2
    def add_edge(self, v1, v2, weight):
        # only need to check one edge for neighbor, because undirected
        if v2 not in self.neighbors[v1]:
            self.neighbors[v1][v2] = weight
            self.neighbors[v2][v1] = weight

    # returns vertex's neighbors
    def get_neighbors(self, vertex):
        return self.neighbors[vertex]
