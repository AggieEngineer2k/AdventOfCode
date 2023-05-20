import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARNING)
import json

class Script:
    def iterate(self, element, total : int = 0, skipRed : bool = False) -> int:
        if isinstance(element, list):
            for i in element:
                total = self.iterate(i, total, skipRed)
            return total
        elif isinstance(element, dict):
            if (skipRed == False or 'red' not in list(element.values())):
                for (k,v) in element.items():
                    total = self.iterate(v, total, skipRed)
            return total
        elif isinstance(element, str):
            return total
        elif isinstance(element, int):
            return total + element
        else:
            raise Exception(f'Unsupported element type "{type(element)}"')
    def parse_input(self, input):
        return json.loads(input)
    def __init__(self, input : str = ""):
        self.input = input
    def day_1(self):
        jsonObject = self.parse_input(self.input)
        total = self.iterate(jsonObject)
        print(f"Day 1: {total}")
    def day_2(self):
        jsonObject = self.parse_input(self.input)
        total = self.iterate(jsonObject, skipRed=True)
        print(f"Day 2: {total}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_line(input_path)

script = Script(input)
script.day_1()
script.day_2()