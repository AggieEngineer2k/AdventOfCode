import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARN)
import re

class Script:
    def get_characters_in_code(self, line : str) -> int:
        return len(line)
    def get_characters_in_memory(self, line : str) -> int:
        return len(eval(line))
    def get_encoded(self, line : str) -> str:
        result = '"'
        for char in line:
            if char == '"':
                result += '\\"'
            elif char == '\\':
                result += '\\\\'
            else:
                result += char
        result += '"'
        return result
    def get_characters_in_encoded(self, line : str) -> int:
        return len(self.get_encoded(line))
    def get_difference_of_characters_in_code_and_memory(self, lines : "list[str]") -> int:
        total_characters_in_code = 0
        total_characters_in_memory = 0
        for line in lines:
            total_characters_in_code += self.get_characters_in_code(line)
            total_characters_in_memory += self.get_characters_in_memory(line)
        return total_characters_in_code - total_characters_in_memory
    def get_difference_of_characters_in_encoded_and_original(self, lines : "list[str]") -> int:
        total_characters_in_encoded = 0
        total_characters_in_original = 0
        for line in lines:
            total_characters_in_encoded += self.get_characters_in_encoded(line)
            total_characters_in_original += len(line)
        return total_characters_in_encoded - total_characters_in_original
    def __init__(self, input : "list[str]" = []):
        self.input = input
    def day_1(self):
        day_1 = self.get_difference_of_characters_in_code_and_memory(self.input)
        print(f"Day 1: {day_1}")
    def day_2(self):
        day_2 = self.get_difference_of_characters_in_encoded_and_original(self.input)
        print(f"Day 2: {day_2}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1()
script.day_2()