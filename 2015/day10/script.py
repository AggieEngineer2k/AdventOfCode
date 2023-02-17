import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARN)

class Script:
    def look_and_say(self, sequence : str) -> str:
        new_sequence = ""
        count = 0
        numeral = ""
        for i in sequence:
            if count == 0:
                count = 1
                numeral = i
            else:
                if i == numeral:
                    count += 1
                else:
                    new_sequence += f"{count}{numeral}"
                    count = 1
                    numeral = i
        new_sequence += f"{count}{numeral}"
        return new_sequence
    def __init__(self, input : str = ""):
        self.input = input
    def day_1(self):
        sequence = self.input
        for i in range(40):
            sequence = self.look_and_say(sequence)
        length = len(sequence)
        print(f"Day 1: {length}")
    def day_2(self):
        sequence = self.input
        for i in range(50):
            sequence = self.look_and_say(sequence)
        length = len(sequence)
        print(f"Day 2: {length}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_line(input_path)

script = Script(input)
script.day_1()
script.day_2()