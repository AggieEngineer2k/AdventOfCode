import logging
logging.basicConfig(level=logging.DEBUG)
import re
from collections import namedtuple

Coordinate = namedtuple("Coordinate", "x y")

def manhattan_distance(from_coordinate : Coordinate, to_coordinate : Coordinate) -> int:
    return abs(to_coordinate.x - from_coordinate.x) + abs(to_coordinate.y - from_coordinate.y)

class Sensor():
    def __init__(self, coordinate : Coordinate, beacon_coordinate : Coordinate) -> None:
        self.coordinate = coordinate
        self.beacon_coordinate = beacon_coordinate
        self.distance = manhattan_distance(coordinate,beacon_coordinate)
    def coordinatesInRange(self, limit_to_row : int = None) -> 'set[Coordinate]':
        coordinates = set()
        for y in range(0,self.distance + 1,1):
            if limit_to_row != None and (self.coordinate.y + y != limit_to_row and self.coordinate.y - y != limit_to_row):
                logging.debug(f'y = {y}; {self.coordinate.y} +- {y} != {inspection_row}; skipping')
                continue
            logging.debug(f'y = {y}; {self.coordinate.y} +- {y} == {inspection_row}; inspecting')
            for x in range(-(self.distance-y),self.distance-y + 1,1):
                if limit_to_row == None or self.coordinate.y + y == limit_to_row:
                    logging.debug(f'x = {x}: ({self.coordinate.x + x},{self.coordinate.y + y})')
                    coordinates.add(Coordinate(self.coordinate.x + x,self.coordinate.y + y))
                if limit_to_row == None or self.coordinate.y - y == limit_to_row:
                    logging.debug(f'x = {x}: ({self.coordinate.x + x},{self.coordinate.y - y})')
                    coordinates.add(Coordinate(self.coordinate.x + x,self.coordinate.y - y))
        coordinates.discard(self.coordinate)
        coordinates.discard(self.beacon_coordinate)
        return coordinates
    def coordinatesAtDistance(self, distance : int):
        coordinates = set()
        for d in range(0,distance + 1):
            coordinates.add(Coordinate(self.coordinate.x - (distance - d), self.coordinate.y - d))
            coordinates.add(Coordinate(self.coordinate.x + (distance - d), self.coordinate.y - d))
            coordinates.add(Coordinate(self.coordinate.x - (distance - d), self.coordinate.y + d))
            coordinates.add(Coordinate(self.coordinate.x + (distance - d), self.coordinate.y + d))
        return coordinates

sensors : 'list[Sensor]' = list()

with open('input.txt','r') as inputFile:
    lines = [line.rstrip() for line in inputFile]

inspection_row = 2000000
inspection_coordinates = set()
for line in lines:
    coordinates = re.findall(r'-?\d+',line)
    sensor_coord = Coordinate(int(coordinates[0]),int(coordinates[1]))
    beacon_coord = Coordinate(int(coordinates[2]),int(coordinates[3]))
    logging.debug(f'{line} : {coordinates}')
    sensor = Sensor(sensor_coord, beacon_coord)
    sensors.append(sensor)

# # Part 1
# for sensor in sensors:
#     logging.info(f'{sensor.coordinate} {sensor.distance}')
#     [inspection_coordinates.add(coordinate) for coordinate in sensor.coordinatesInRange(inspection_row)]
# print(f'{len(inspection_coordinates)}')

# Part 2
# Outline each sensor's region, then check each coordinate to see if it's included in at least one other sensor's region. If not, that's the distress beacon.
def part2(minimum_coordinate, maximum_coordinate):
    for from_sensor in sensors:
        coordinates_at_distance = from_sensor.coordinatesAtDistance(from_sensor.distance + 1)
        logging.debug(f'trying {len(coordinates_at_distance)} coordinates around {from_sensor.coordinate}...')
        for coordinate in coordinates_at_distance:
            if coordinate.x < minimum_coordinate or coordinate.x > maximum_coordinate or coordinate.y < minimum_coordinate or coordinate.y > maximum_coordinate:
                continue
            found_coordinate : bool = True
            for to_sensor in sensors:
                if from_sensor == to_sensor:
                    continue
                if manhattan_distance(coordinate,to_sensor.coordinate) <= to_sensor.distance:
                    found_coordinate = False
                    break
            if found_coordinate == True:
                logging.debug(f'{coordinate} is not in range of any sensor!')
                return coordinate

coordinate = part2(0,4000000)
tuning_frequecy = coordinate.x * 4000000 + coordinate.y
print(f'{tuning_frequecy}')