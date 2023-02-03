import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser

class script:
    def floor_change(self, instruction : str):
        if instruction == "(":
            return 1
        elif instruction == ")":
            return -1
    def determine_floor(self, instructions : str):
        value = 0
        for instruction in instructions:
            value += self.floor_change(instruction)
        return value
    def determine_instruction_that_enters_basement(self, instructions : str):
        value = 0
        for i in range(0,len(instructions)):
            value += self.floor_change(instructions[i])
            if value < 0:
                return i + 1
            i += 1
    def __init__(self, input : str = ""):
        self.input = input
        pass
    def part_1(self):
        floor = self.determine_floor(self.input)
        print(f"Day 1: {floor}")
    def part_2(self):
        floor = self.determine_instruction_that_enters_basement(self.input)
        print(f"Day 2: {floor}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_line(input_path)

solver = script(input)
solver.part_1()
solver.part_2()