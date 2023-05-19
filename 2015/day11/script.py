import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARNING)

class Script:
    def get_next_password(self, input) -> str:
        result = input
        while True:
            result = self.increment_string(result)
            result = self.sanitize_string(result)
            if(len(result) > 8):
                raise Exception('No password found.')
            if (self.check_is_valid(result)):
                return result
    def check_is_valid(self, input) -> bool:
        return self.check_contains_straight(input) and self.check_contains_valid_characters(input) and self.check_contains_two_pairs(input) and len(input) == 8
    def check_contains_straight(self, input) -> bool:
        for substring in [input[i:i+3] for i in range(0,len(input)-2)]:
            if (ord(substring[0]) == ord(substring[1]) - 1 and ord(substring[1]) == ord(substring[2]) - 1):
                return True
        return False
    def check_contains_valid_characters(self, input) -> bool:
        return not('i' in input or 'o' in input or 'l' in input)
    def check_contains_two_pairs(self, input) -> bool:
        result = input
        while (result[0] != result[1] and len(result) > 4):
            result = result[1:]
        if (result[0] != result[1]):
            return False
        while (result[0] != result[2] and result[2] != result[3] and len(result) > 4):
            result = result[:2] + result[3:]
        if (result[0] == result[2] or result[2] != result[3]):
            return False
        return True
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
        next_password = self.get_next_password(self.input)
        print(f"Day 1: {next_password}")
    def day_2(self):
        next_password = self.get_next_password(self.input)
        next_password = self.get_next_password(next_password)
        print(f"Day 2: {next_password}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_line(input_path)

script = Script(input)
script.day_1()
script.day_2()