import logging
logging.basicConfig(level=logging.INFO)
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

for sensor in sensors:
    logging.info(f'{sensor.coordinate} {sensor.distance}')
    [inspection_coordinates.add(coordinate) for coordinate in sensor.coordinatesInRange(inspection_row)]
    
print(f'{len(inspection_coordinates)}')