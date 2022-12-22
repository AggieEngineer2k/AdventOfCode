import logging
logging.basicConfig(level=logging.WARN)
import re
from collections import namedtuple

AIR = '.'
ROCK = '#'
GRAIN = 'o'
SAND_SETTLED = 1
SAND_FALLING_INTO_ABYSS = 0
SAND_BLOCKED = -1

source_row = 0
source_column = 500

cave = [[AIR for column in range(source_column * 2)] for row in range(200)]
Point = namedtuple('Point','row column')

def addRocks(coordinates : "list[Point]"):
    if len(coordinates) <= 1:
        return
    rock_from = coordinates[0]
    rock_to = coordinates[1]
    for row in range(min(int(rock_from.row),int(rock_to.row)),max(int(rock_from.row),int(rock_to.row)) + 1):
        for column in range(min(int(rock_from.column),int(rock_to.column)),max(int(rock_from.column),int(rock_to.column)) + 1):
            logging.debug(f'# @ ({row},{column})')
            cave[row][column] = ROCK
    addRocks(coordinates[1:])

def moveSand(point : Point, grain : int):
    logging.info(f'Grain {grain} is at ({point.row},{point.column})')
    if cave[source_row][source_column] == GRAIN:
        logging.info(f'Grain {grain} is blocked.')
        return SAND_BLOCKED
    elif point.row > 200:
        logging.info(f'Grain {grain} is falling into the abyss.')
        return SAND_FALLING_INTO_ABYSS
    elif cave[point.row + 1][point.column] == AIR:
        logging.info(f'Grain {grain} is falling down.')
        return moveSand(Point(point.row + 1,point.column),grain)
    elif cave[point.row + 1][point.column - 1] == AIR:
        logging.info(f'Grain {grain} is falling down-left.')
        return moveSand(Point(point.row + 1,point.column - 1),grain)
    elif cave[point.row + 1][point.column + 1] == AIR:
        logging.info(f'Grain {grain} is falling down-right.')
        return moveSand(Point(point.row + 1,point.column + 1),grain)
    else:
        logging.info(f'Grain {grain} is settled.')
        cave[point.row][point.column] = GRAIN
        return SAND_SETTLED

def show():
    with open('cave.txt','w') as f:
        #[print(''.join(row) + '\n') for row in cave[:10]]
        [f.write(''.join(row) + '\n') for row in cave]

with open('input.txt','r') as inputFile:
    lines = [line.rstrip() for line in inputFile]

lowest_rock = 0
for line in lines:
    coordinates = [Point(row,column) for column,row in zip(*[iter(re.findall(r'\d+',line))]*2)]
    addRocks(coordinates)
    lowest_rock = max(lowest_rock,max([int(point.row) for point in coordinates]))
addRocks([Point(lowest_rock + 2,0),Point(lowest_rock + 2,len(cave[0])-1)])

i = 0
result = SAND_SETTLED
while result == SAND_SETTLED:
    i += 1
    result = moveSand(Point(source_row,source_column),i)
show()
print(f'{i - 1} grains settled.')