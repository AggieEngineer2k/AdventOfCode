class Vertex:
    def __init__(self, height : str) -> None:
        self.height = height
        self.visited = False
        self.distance = float('inf')
        # Reference to the previous vertex in the shortest path.
        self.parent : Vertex = None
        # Reference to the starting vertex.

class Graph:
    def __init__(self, vertices) -> None:
        # Store the graph of vertices.
        self.vertices = [[Vertex(column) for column in row] for row in vertices]
        # Create a set for storing the vertices in the shortest path.
        self.shortest_path_tree = set()

    def findVerticesByHeight(self,height : str):
        return [(vertex,irow,icolumn) for irow, row in enumerate(self.vertices) for icolumn, vertex in enumerate(row) if vertex.height == height]

    def findShortestPath(self,starting : str,ending : str):
        # Find the starting vertex.
        start = self.findVerticesByHeight(starting)[0][0]
        # Set the start vertex's distance to 0.
        start.distance = 0

        # Find the ending vertex.
        end = self.findVerticesByHeight(ending)[0][0]

        # Start searching from the starting vertex and continue searching until the ending vertex is the next to be visited.
        current = start
        #while current != end:

    def show(self):
        [print(' '.join([str(vertex.height) for vertex in row])) for row in self.vertices]
        [print(' '.join([str(vertex.visited) for vertex in row])) for row in self.vertices]
        [print(' '.join([str(vertex.distance) for vertex in row])) for row in self.vertices]

graph : Graph
with open('input.txt','r') as inputFile:
    graph = Graph(vertices=[list(line.rstrip()) for line in inputFile])

graph.findShortestPath(starting='S',ending='E')

graph.show()