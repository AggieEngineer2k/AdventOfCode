import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARN)
import re
from collections import namedtuple

Point = namedtuple("Point", "x y")

class Instruction:
    def __init__(self, instruction):
        match = re.match(r"(.+) (\d+),(\d+) through (\d+),(\d+)", instruction)
        self.action = match.group(1)
        self.from_light = Point(int(match.group(2)),int(match.group(3)))
        self.to_light = Point(int(match.group(4)),int(match.group(5)))

class Script:
    lights : "list[list[int]]"
    def reset_lights(self):
        self.lights = [[0 for col in range(self.cols)] for row in range(self.rows)]
    def __init__(self, input : "list[str]" = [], rows : int = 1000, cols : int = 1000):
        self.input = input
        self.rows = rows
        self.cols = cols
        self.reset_lights()
    def follow_instruction_day1(self, instruction : Instruction):
        for row in range(instruction.from_light.y,instruction.to_light.y + 1):
            for col in range(instruction.from_light.x,instruction.to_light.x + 1):
                if instruction.action == "turn on":
                    self.lights[row][col] = 1
                elif instruction.action == "toggle":
                    self.lights[row][col] ^= 1
                elif instruction.action == "turn off":
                    self.lights[row][col] = 0
    def follow_instruction_day2(self, instruction : Instruction):
        for row in range(instruction.from_light.y,instruction.to_light.y + 1):
            for col in range(instruction.from_light.x,instruction.to_light.x + 1):
                if instruction.action == "turn on":
                    self.lights[row][col] += 1
                elif instruction.action == "toggle":
                    self.lights[row][col] += 2
                elif instruction.action == "turn off":
                    self.lights[row][col] = max(0,self.lights[row][col] - 1)
    def day_1(self):
        for line in self.input:
            instruction = Instruction(line)
            script.follow_instruction_day1(instruction)
        number_of_lights_on = 0
        for row in self.lights:
            for light in row:
                if light == 1:
                    number_of_lights_on += 1
        print(f"Day 1: {number_of_lights_on}")
    def day_2(self):
        for line in self.input:
            instruction = Instruction(line)
            script.follow_instruction_day2(instruction)
        total_brightness = 0
        for row in script.lights:
            for light in row:
                total_brightness += light
        print(f"Day 2: {total_brightness}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1()
script.reset_lights()
script.day_2()