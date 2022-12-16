def visible_north(row,column,height):
    if row == 0:
        return forest[row][column] < height
    else:
        return forest[row][column] < height and visible_north(row - 1,column,height)

def visible_south(row,column,height):
    if row == rows - 1:
        return forest[row][column] < height
    else:
        return forest[row][column] < height and visible_south(row + 1,column,height)

def visible_east(row,column,height):
    if column == columns - 1:
        return forest[row][column] < height
    else:
        return forest[row][column] < height and visible_east(row,column + 1,height)

def visible_west(row,column,height):
    if column == 0:
        return forest[row][column] < height
    else:
        return forest[row][column] < height and visible_west(row,column - 1,height)

lines = None
with open('input.txt','r') as input:
    lines = [line.rstrip() for line in input]

forest = list()
for line in lines:
    forest.append([char for char in line])

rows = len(forest)
columns = len(forest[0])
visible_trees = 0
for row in range(0,rows):
    for column in range(0,columns):
        if row == 0 or row == rows - 1 or column == 0 or column == columns - 1:
            visible_trees += 1
        elif visible_north(row - 1,column,forest[row][column]) or visible_south(row + 1,column,forest[row][column]) or visible_east(row,column + 1,forest[row][column]) or visible_west(row,column - 1,forest[row][column]):
            visible_trees += 1

print(visible_trees)