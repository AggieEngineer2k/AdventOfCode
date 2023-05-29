import logging
logging.basicConfig(level=logging.WARN)
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
from common.coordinate import Coordinate

class Santa:
    def __init__(self):
        self.coordinate = Coordinate()
        self.houses = list()
        self.add_house()
    def get_house(self):
        return self.coordinate.get_tuple()
    def add_house(self):
        self.houses.append(self.get_house())
    def move(self, direction : str):
        if direction == '^':
            self.coordinate = Coordinate(self.coordinate.x, self.coordinate.y + 1)
        elif direction == 'v':
            self.coordinate = Coordinate(self.coordinate.x, self.coordinate.y - 1)
        elif direction == '<':
            self.coordinate = Coordinate(self.coordinate.x - 1, self.coordinate.y)
        elif direction == '>':
            self.coordinate = Coordinate(self.coordinate.x + 1, self.coordinate.y)
        self.add_house()
        return self.get_house()
    def get_visited_houses(self):
        return set(self.houses)
    def get_number_of_visited_houses(self):
        return len(self.get_visited_houses())

class script:
    def __init__(self, input : str):
        self.input = input
    def day_1(self):
        santa = Santa()
        [santa.move(i) for i in self.input]
        number_of_visited_houses = santa.get_number_of_visited_houses()
        print(f"Day 1: {number_of_visited_houses}")
    def day_2(self):
        santa = Santa()
        robo_santa = Santa()
        [santa.move(i) for i in self.input[::2]]
        [robo_santa.move(i) for i in self.input[1::2]]
        visited_houses = santa.get_visited_houses()
        visited_houses.update(robo_santa.get_visited_houses())
        number_of_visited_houses = len(visited_houses)
        print(f"Day 2: {number_of_visited_houses}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_line(input_path)

solver = script(input)
solver.day_1()
solver.day_2()