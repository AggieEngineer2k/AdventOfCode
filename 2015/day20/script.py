import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.DEBUG)
from common.math import *

class Script:
    input : int
    def __init__(self, input : str = ""):
        self.input = int(input) if input else None
    def presents(self, house : int) -> int:
        elves = factors(house)
        return sum([elf * 10 for elf in elves])
    def presents_day2(self, house : int) -> int:
        elves = [elf for elf in factors(house) if house // elf <= 50]
        return sum([elf * 11 for elf in elves])
    def day_1(self):
        house = 0
        while True:
            house = house + 1
            presents = self.presents(house)
            if house % 10000 == 0:
                logging.debug(f"PART 1: House {house:10} received {presents:10}.")
            if presents >= self.input:
                break
        print(f"Day 1: {house}")
    def day_2(self):
        house = 0
        while True:
            house = house + 1
            presents = self.presents_day2(house)
            if house % 10000 == 0:
                logging.debug(f"PART 2: House {house:10} received {presents:10}.")
            if presents >= self.input:
                break
        print(f"Day 2: {house}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_line(input_path)

script = Script(input)
script.day_1()
script.day_2()