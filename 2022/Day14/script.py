import logging
logging.basicConfig(level=logging.WARN)
import re
from collections import namedtuple

AIR = '.'
ROCK = '#'
GRAIN = 'o'
SAND_SETTLED = 1
SAND_FALLING_INTO_ABYSS = 0

cave = [[AIR for column in range(600)] for row in range(250)]
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
    if point.row > 200:
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
    [print(''.join(row)) for row in cave]

with open('input.txt','r') as inputFile:
    lines = [line.rstrip() for line in inputFile]
for line in lines:
    coordinates = [Point(row,column) for column,row in zip(*[iter(re.findall(r'\d+',line))]*2)]
    addRocks(coordinates)

i = 0
result = SAND_SETTLED
while result == SAND_SETTLED:
    i += 1
    result = moveSand(Point(0,500),i)
print(f'Part 1: {i - 1} grains settled.')