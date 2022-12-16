import matplotlib.pyplot as plt
import time

class Coordinate:
    x : int = 0
    y : int = 0
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
    def moveUp(self):
        self.y += 1
    def moveDown(self):
        self.y -= 1
    def moveLeft(self):
        self.x -= 1
    def moveRight(self):
        self.x += 1

# Head and tail X/Y coordinates starting at midpoint of grid.
coordinates = [
    # Part 1
    Coordinate(0,0), #  1
    Coordinate(0,0), #  2
    # Part 2
    Coordinate(0,0), #  3
    Coordinate(0,0), #  4
    Coordinate(0,0), #  5
    Coordinate(0,0), #  6
    Coordinate(0,0), #  7
    Coordinate(0,0), #  8
    Coordinate(0,0), #  9
    Coordinate(0,0)  # 10
]
positions = set()

def moveKnotX(index : int):
    global coordinates
    knot = coordinates[index]
    lead = coordinates[index - 1]
    knot.x += (lead.x - knot.x) // abs((lead.x - knot.x))

def moveKnotY(index : int):
    global coordinates
    knot = coordinates[index]
    lead = coordinates[index - 1]
    knot.y += (lead.y - knot.y) // abs((lead.y - knot.y))

def moveKnot(index):
    global coordinates, positions
    knot = coordinates[index]
    lead = coordinates[index - 1]
    dx = abs(lead.x - knot.x)
    dy = abs(lead.y - knot.y)

    if dx == 2 and dy == 2:
        moveKnotX(index)
        moveKnotY(index)
    elif dx == 2 and dy == 1:
        moveKnotX(index)
        moveKnotY(index)
    elif dx == 1 and dy == 2:
        moveKnotX(index)
        moveKnotY(index)
    elif dx == 2 and dy == 0:
        moveKnotX(index)
    elif dx == 0 and dy == 2:
        moveKnotY(index)

    if index == len(coordinates) - 1:
        positions.add((knot.x, knot.y))
    else:
        moveKnot(index + 1)
        
def moveHead(direction : str, distance : int):
    global coordinates
    head = coordinates[0]
    # Move the head one step at a time.
    if direction == 'U':
        coordinates[0].moveUp()
    elif direction == 'D':
        coordinates[0].moveDown()
    elif direction == 'L':
        coordinates[0].moveLeft()
    elif direction == 'R':
        coordinates[0].moveRight()
    # Move all the remaining knots, beginning with the one directly behind the head.
    moveKnot(1)
    # Continue moving the head if there are steps left to finish moving the full distance.
    if(distance > 1):
        moveHead(direction,distance - 1)
        
plt.ion()
fig = plt.figure()
ax = fig.add_subplot()
plt.xlim([-10, 10])
plt.ylim([-10, 10])
line1, = ax.plot([coordinate.x for coordinate in coordinates],[coordinate.y for coordinate in coordinates],linestyle='--', marker='o')
        
lines = None
with open('input.txt','r') as inputFile:
    lines = [line.rstrip() for line in inputFile]
for line in lines:
    tokens = line.split()
    moveHead(tokens[0],int(tokens[1]))
    line1.set_xdata([coordinate.x for coordinate in coordinates])
    line1.set_ydata([coordinate.y for coordinate in coordinates])
    plt.xlim([min([coordinate.x for coordinate in coordinates]) - 5,max([coordinate.x for coordinate in coordinates]) + 5])
    plt.ylim([min([coordinate.y for coordinate in coordinates]) - 5,max([coordinate.y for coordinate in coordinates]) + 5])
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.25)

print(len(positions))

input()