import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARNING)
import re

class Script:
    def extract_numbers(self, input) -> "list[int]":
        return [int(x) for x in re.findall('(-?\d+)',input)]
    def __init__(self, input : str = ""):
        self.input = input
    def day_1(self):
        result = sum(self.extract_numbers(self.input))
        print(f"Day 1: {result}")
    def day_2(self):
        print(f"Day 2: ")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_line(input_path)

script = Script(input)
script.day_1()
script.day_2()