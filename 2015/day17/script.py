import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARNING)
from itertools import combinations

class Script:
    def __init__(self, input : "list[str]" = []):
        self.input = input
    def day_1(self):
        set = list([int(line) for line in self.input])
        combos = [combination for cardinality in range(len(set)) for combination in combinations(set,cardinality+1) if sum(combination) == 150]
        print(f"Day 1: {len(combos)}")
    def day_2(self):
        set = list([int(line) for line in self.input])
        combos = [combination for cardinality in range(len(set)) for combination in combinations(set,cardinality+1) if sum(combination) == 150]
        min_cardinality = min([len(combination) for combination in combos])
        count = len([1 for combination in combos if len(combination) == min_cardinality])
        print(f"Day 2: {count}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1()
script.day_2()