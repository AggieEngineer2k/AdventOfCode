import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARN)

class Script:
    def check_contains_straight(self, input) -> bool:
        for substring in [input[i:i+3] for i in range(0,len(input)-2)]:
            if (ord(substring[0]) == ord(substring[1]) - 1 and ord(substring[1]) == ord(substring[2]) - 1):
                return True
        return False
    def sanitize_string(self, input) -> str:
        index = -1
        for x in ['i','o','l']:
            i = input.find(x)
            if (i > -1 and (index == -1 or i < index)):
                index = i
        result = input
        if (index > -1):
            result = result[:index] + chr(ord(result[index]) + 1) + (((len(result) - index - 1)) * 'a')
        return result
    def increment_string(self, input) -> str:
        if (input == 'z'):
            result = 'aa'
        elif (input[-1] == 'z'):
            result = self.increment_string(input[:-1]) + 'a'
        else:
            result = input[:-1] + chr(ord(input[-1]) + 1)
        return result
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