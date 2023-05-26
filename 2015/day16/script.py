import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARNING)
import re

class Sue:
    def __init__(self, input : str = "", number : int = None, attributes : dict = None):
        if attributes is None:
            attributes = {}
        self.number = number
        self.attributes = attributes
        if re.match(r"Sue \d+:(?:\s\w+: \d+,?)+", input):
            result = re.search(r"Sue (\d+):", input)
            self.number = int(result.group(1))
            results = re.findall(r"(\w+): (\d+)", input)
            self.attributes.clear()
            for result in results:
                self.attributes.update({result[0]: int(result[1])})
    def __eq__(self, other): 
        if not isinstance(other, Sue):
            return NotImplemented
        return self.number == other.number \
            and self.attributes == other.attributes
    def __str__(self) -> str:
        return f"Sue {self.number}: {self.attributes}"

class Script:
    aunts : "list[Sue]"
    def __init__(self, input : "list[str]" = []):
        self.input = input
    def parse_input(self, input : "list[str]" = []) -> "list[Sue]":
        result = []
        for line in input:
            result.append(Sue(input = line))
        return result
    def day_1(self):
        aunts = self.parse_input(self.input)
        gifter = {        
            'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1
        }
        for attribute in gifter:
            for i in reversed(range(len(aunts))):
                if attribute in aunts[i].attributes.keys() and aunts[i].attributes[attribute] != gifter[attribute]:
                    aunts.pop(i)
        print(f"Day 1: {aunts[0]}")
    def day_2(self):
        aunts = self.parse_input(self.input)
        gifter = {        
            'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1
        }
        for attribute in gifter:
            for i in reversed(range(len(aunts))):
                if attribute not in aunts[i].attributes.keys():
                    continue
                if attribute in ['cats','trees']:
                    if aunts[i].attributes[attribute] <= gifter[attribute]:
                        aunts.pop(i)
                elif attribute in ['pomeranians','goldfish']:
                    if aunts[i].attributes[attribute] >= gifter[attribute]:
                        aunts.pop(i)
                elif aunts[i].attributes[attribute] != gifter[attribute]:
                    aunts.pop(i)
        print(f"Day 2: {aunts[0]}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1()
script.day_2()