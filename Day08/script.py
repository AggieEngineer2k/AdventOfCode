def isVisibleFromNorth(row,column,height):
    if row == 0:
        return forest[row][column] < height
    else:
        return forest[row][column] < height and isVisibleFromNorth(row - 1,column,height)

def isVisibleFromSouth(row,column,height):
    if row == rows - 1:
        return forest[row][column] < height
    else:
        return forest[row][column] < height and isVisibleFromSouth(row + 1,column,height)

def isVisibleFromEast(row,column,height):
    if column == columns - 1:
        return forest[row][column] < height
    else:
        return forest[row][column] < height and isVisibleFromEast(row,column + 1,height)

def isVisibleFromWest(row,column,height):
    if column == 0:
        return forest[row][column] < height
    else:
        return forest[row][column] < height and isVisibleFromWest(row,column - 1,height)

def scoreFromNorth(row,column,height,score : int = 0) -> int:
    score += 1
    if row == 0 or forest[row][column] >= height:
        return score
    else:
        return scoreFromNorth(row - 1,column,height,score)

def scoreFromSouth(row,column,height,score : int = 0) -> int:
    score += 1
    if row == rows - 1 or forest[row][column] >= height:
        return score
    else:
        return scoreFromSouth(row + 1,column,height,score)

def scoreFromEast(row,column,height,score : int = 0) -> int:
    score += 1
    if column == columns - 1 or forest[row][column] >= height:
        return score
    else:
        return scoreFromEast(row,column + 1,height,score)

def scoreFromWest(row,column,height,score : int = 0) -> int:
    score += 1
    if column == 0 or forest[row][column] >= height:
        return score
    else:
        return scoreFromWest(row,column - 1,height,score)

lines = None
with open('input.txt','r') as input:
    lines = [line.rstrip() for line in input]

forest = list()
for line in lines:
    forest.append([char for char in line])

rows = len(forest)
columns = len(forest[0])

visible_trees = 0
for row in range(rows):
    for column in range(columns):
        if row == 0 or row == rows - 1 or column == 0 or column == columns - 1:
            visible_trees += 1
        elif isVisibleFromNorth(row - 1,column,forest[row][column]) \
            or isVisibleFromSouth(row + 1,column,forest[row][column]) \
            or isVisibleFromEast(row,column + 1,forest[row][column]) \
            or isVisibleFromWest(row,column - 1,forest[row][column]):
            visible_trees += 1

print(f"Part 1: {visible_trees}")

scores = [[None] * columns for i in range(rows)]
for row in range(rows):
    for column in range(columns):
        if row == 0 or row == rows - 1 or column == 0 or column == columns - 1:
            scores[row][column] = 0
        else:
            height = forest[row][column]
            scores[row][column] = \
                scoreFromNorth(row - 1,column,height) \
                * scoreFromSouth(row + 1,column,height) \
                * scoreFromEast(row,column + 1,height) \
                * scoreFromWest(row,column - 1,height)

print(f"Part 2: {max(map(max, scores))}")