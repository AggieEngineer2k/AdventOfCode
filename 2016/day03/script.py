import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARNING)
import re

class Script:
    input : "list(str)"
    def parseLine(self, line : str) -> "list(int)":
        sides = [int(x) for x in re.findall(r"(\d+)",line)]
        return sides
    def isTriangle(self, sides : "list(int)") -> bool:
        return (sides[0] + sides[1] > sides[2]) and (sides[1] + sides[2] > sides[0]) and (sides[2] + sides[0] > sides[1])
    def __init__(self, input : str = []):
        self.input = input
    def day_1(self):
        triangles = 0
        for line in self.input:
            sides = self.parseLine(line)
            if self.isTriangle(sides):
                triangles = triangles + 1
        print(f"Day 1: {triangles}")
    def day_2(self):
        triangles = 0
        for i in range(int(len(self.input) / 3)):
            lines = [self.parseLine(self.input[i * 3 + x]) for x in range(3)]
            sides = [[lines[x][y] for x in range(3)] for y in range(3)]
            logging.debug(f"lines: {lines}")
            logging.debug(f"sides: {sides}")
            for lengths in sides:
                if self.isTriangle(lengths):
                    triangles = triangles + 1
        print(f"Day 2: {triangles}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1()
script.day_2()