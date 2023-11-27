import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARNING)

class Script:
    input : "list(str)"
    keypad = [
        ["1","2","3"],
        ["4","5","6"],
        ["7","8","9"]
    ]
    row = 1
    column = 1
    def __init__(self, input : str = []):
        self.input = input
    def move(self, instruction : str):
        if instruction == 'U':
            self.row = max(0, self.row - 1)
        elif instruction == 'D':
            self.row = min(2, self.row + 1)
        elif instruction == 'L':
            self.column = max(0, self.column - 1)
        elif instruction == 'R':
            self.column = min(2, self.column + 1)
    def day_1(self):
        code = ""
        for line in input:
            for instruction in line:
                self.move(instruction)
            code = code + self.keypad[self.row][self.column]
        print(f"Day 1: {code}")
    def day_2(self):
        print(f"Day 2: ")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1()
script.day_2()