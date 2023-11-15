import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARNING)
from common.coordinate import Coordinate
import re

class Turtle:
    coordinate : Coordinate = Coordinate()
    facing : str = "N"
    stopAtFirstRepeat : bool
    visited : "list[Coordinate]"
    def __init__(self, stopAtFirstRepeat : bool = False):
        self.stopAtFirstRepeat = stopAtFirstRepeat
        self.visited = [self.coordinate]
    def displacement(self) -> float:
        return abs(self.coordinate.x) + abs(self.coordinate.y)
    def move(self, directions : str):
        start_coordinate = self.coordinate
        start_facing = self.facing
        m = re.match(r"(?P<turn>\w)(?P<distance>\d+)", directions).groupdict()
        turn = m['turn']
        distance = int(m['distance'])
        if self.facing == "N":
            if turn == "L":
                self.facing = "W"
            elif turn == "R":
                self.facing = "E"
        elif self.facing == "E":
            if turn == "L":
                self.facing = "N"
            elif turn == "R":
                self.facing = "S"
        elif self.facing == "S":
            if turn == "L":
                self.facing = "E"
            elif turn == "R":
                self.facing = "W"
        elif self.facing == "W":
            if turn == "L":
                self.facing = "S"
            elif turn == "R":
                self.facing = "N"
        logging.debug(f"Started at {start_coordinate} facing {start_facing}; turning {turn} to face {self.facing}, moving {distance}.")
        for x in range(0,distance):
            if self.facing == "N":
                self.coordinate = Coordinate(self.coordinate.x, self.coordinate.y + 1)
            elif self.facing == "E":
                self.coordinate = Coordinate(self.coordinate.x + 1, self.coordinate.y)
            elif self.facing == "S":
                self.coordinate = Coordinate(self.coordinate.x, self.coordinate.y - 1)
            elif self.facing == "W":
                self.coordinate = Coordinate(self.coordinate.x - 1, self.coordinate.y)
            logging.debug(f"  Visiting {self.coordinate}.")
            if(self.stopAtFirstRepeat and (self.coordinate in self.visited)):
                logging.debug(f"    Already visited {self.coordinate}.")
                return True
            else:
                self.visited.append(self.coordinate)
        logging.debug(f"  Ended at {self.coordinate} facing {self.facing}.")
        return False

class Script:
    input : str
    directions : "list[str]"
    def __init__(self, input : str = ""):
        self.input = input
        self.steps = self.parseInput(self.input)
    def parseInput(self, input : str) -> "list[str]":
        return input.split(", ")
    def day_1(self):
        turtle = Turtle()
        [turtle.move(step) for step in self.steps]
        print(f"Day 1: {turtle.displacement()}")
    def day_2(self):
        turtle = Turtle(stopAtFirstRepeat = True)
        for step in self.steps:
            if turtle.move(step):
                break
        print(f"Day 2: {turtle.displacement()}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_line(input_path)

script = Script(input)
script.day_1()
script.day_2()