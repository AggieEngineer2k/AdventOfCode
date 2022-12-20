import logging
logging.basicConfig(level=logging.WARNING)

class Vertex:
    def __init__(self, height : str,row : int,column : int) -> None:
        self.height = height
        self.visited = False
        self.distance = float('inf')
        self.row = row
        self.column = column
        self.path = '.'
        # Reference to the previous vertex in the shortest path.
        self.parent : Vertex = None

class Graph:
    def __init__(self, vertices) -> None:
        # Create the graph of vertices.
        self.vertices = [[Vertex(vertices[r][c],r,c) for c in range(len(vertices[r]))] for r in range(len(vertices))]
        # Inspect the dimensions of the graph.
        self.rows = len(self.vertices)
        self.columns = len(self.vertices[0])
        # Create a set for storing the vertices in the shortest path.
        self.shortest_path_tree = set()

    def findVerticesByHeight(self,height : str):
        return [(vertex,irow,icolumn) for irow, row in enumerate(self.vertices) for icolumn, vertex in enumerate(row) if vertex.height == height]

    def findUnvisitedNeighbors(self,current : Vertex):
        neighbors : list[Vertex] = []
        # North
        if current.row > 0:
            neighbors.append(self.vertices[current.row - 1][current.column])
        # South
        if current.row < self.rows - 1:
            neighbors.append(self.vertices[current.row + 1][current.column])
        # East
        if current.column < self.columns - 1:
            neighbors.append(self.vertices[current.row][current.column + 1])
        # West
        if current.column > 0:
            neighbors.append(self.vertices[current.row][current.column - 1])
        result = [neighbor for neighbor in neighbors if current.height == 'S' or ord(neighbor.height) <= (ord(current.height) + 1) and not neighbor.visited]
        return result

    def findUnvisitedVertexWithSmallestDistance(self):
        unvisited = [vertex for irow, row in enumerate(self.vertices) for icolumn, vertex in enumerate(row) if vertex.visited == False]
        unvisited.sort(key=lambda x: x.distance)
        logging.debug(f'Next to visit is ({unvisited[0].row},{unvisited[0].column})')
        return unvisited[0]

    def findShortestPath(self,starting : str,ending : str):
        # Find the starting vertex.
        start = self.findVerticesByHeight(starting)[0][0]
        # Set the start vertex's distance to 0.
        start.distance = 0
        start.path = 'S'

        # Find the ending vertex.
        end = self.findVerticesByHeight(ending)[0][0]
        end.path = 'E'

        # Start searching from the starting vertex and continue searching until the ending vertex is the next to be visited.
        current = start
        while current != end:
            logging.debug(f'Visiting ({current.row},{current.column}) at distance {current.distance}')
            distance_through_current = current.distance + 1
            for neighbor in self.findUnvisitedNeighbors(current):
                logging.debug(f'{neighbor.distance} > {distance_through_current}')
                if neighbor.distance > distance_through_current:
                    neighbor.distance = distance_through_current
                    neighbor.parent = current
                    if(neighbor.row < current.row):
                        neighbor.path = '^'
                    elif(neighbor.row > current.row):
                        neighbor.path = 'V'
                    elif(neighbor.column > current.column):
                        neighbor.path = '>'
                    elif(neighbor.column < current.column):
                        neighbor.path = '<'
            current.visited = True
            current = self.findUnvisitedVertexWithSmallestDistance()
        return end

    def show(self):
        #[print(' '.join([str(vertex.height) for vertex in row])) for row in self.vertices]
        #[print(' '.join(['({row},{column})'.format(row=vertex.row,column=vertex.column) for vertex in row])) for row in self.vertices]
        #[print(' '.join(['o' if vertex.visited else '.' for vertex in row])) for row in self.vertices]
        #[print(' '.join([str(vertex.distance) for vertex in row])) for row in self.vertices]
        [print(''.join([str(vertex.path) for vertex in row])) for row in self.vertices]

graph : Graph
with open('input.txt','r') as inputFile:
    graph = Graph(vertices=[list(line.rstrip()) for line in inputFile])

end = graph.findShortestPath(starting='S',ending='E')
#graph.show()
print(f"'E' is {end.distance} from 'S'.")