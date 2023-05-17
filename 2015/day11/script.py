import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARN)

class Script:
    def increment_string(self, input) -> str:
        return input
    def __init__(self, input : str = ""):
        self.input = input
    def day_1(self):
        print(f"Day 1:")
    def day_2(self):
        print(f"Day 2:")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_line(input_path)

script = Script(input)
script.day_1()
script.day_2()