# Head and tail X/Y coordinates starting at midpoint of grid.
hx = hy = tx = ty = 0
positions = set()

def moveHead(direction : str, distance : int):
    global hx, hy
    if direction == 'U':
        hy += 1
    elif direction == 'D':
        hy -= 1
    elif direction == 'L':
        hx -= 1
    elif direction == 'R':
        hx += 1
    moveTail()
    if(distance > 1):
        moveHead(direction,distance - 1)

def moveTailX():
    global hx, tx
    tx += (hx - tx) // abs((hx - tx))

def moveTailY():
    global hy, ty
    ty += (hy - ty) // abs((hy - ty))

def moveTail():
    global hx, hy, tx, ty, positions
    if abs(hx - tx) == 2 and abs(hy - ty) == 2:
        moveTailX()
        moveTailY()
    elif abs(hx - tx) == 2 and abs(hy - ty) == 1:
        moveTailX()
        moveTailY()
    elif abs(hx - tx) == 1 and abs(hy - ty) == 2:
        moveTailX()
        moveTailY()
    elif abs(hx - tx) == 2 and abs(hy - ty) == 0:
        moveTailX()
    elif abs(hx - tx) == 0 and abs(hy - ty) == 2:
        moveTailY()
    positions.add((tx,ty))
    #print(f"H:({hx},{hy}) T:({tx},{ty})")
        
lines = None
with open('input.txt','r') as input:
    lines = [line.rstrip() for line in input]
for line in lines:
    tokens = line.split()
    moveHead(tokens[0],int(tokens[1]))

print(len(positions))