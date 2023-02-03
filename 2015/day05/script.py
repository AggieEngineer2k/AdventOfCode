import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARN)
import re

class script:
    def has_three_vowels(self, string : str) -> bool:
        return len(re.findall('[aeiou]',string)) >= 3
    def has_double_letter(self, string : str) -> bool:
        return True in [string[i]==string[i-1] for i in range(1,len(string))]
    def has_forbidden(self, string : str, forbidden : "list[str]") -> bool:
        return len(set([string[i-1:i+1] for i in range(1,len(string))]).intersection(forbidden)) > 0
    def is_nice_day1(self, string : str) -> bool:
        forbidden = ['ab','cd','pq','xy']
        return self.has_three_vowels(string) and self.has_double_letter(string) and not self.has_forbidden(string,forbidden)
    def has_repeated_substring(self, string : str) -> bool:
        return True in [string.find(string[i:i+2],i+2) > -1 for i in range(len(string)-1)]
    def has_split_letter(self, string : str) -> bool:
        return True in [string[i]==string[i+2] for i in range(len(string)-2)]
    def is_nice_day2(self, string : str) -> bool:
        return self.has_repeated_substring(string) and self.has_split_letter(string)
    def __init__(self, input : str = ""):
        self.input = input
    def day_1(self):
        number_of_nice = [self.is_nice_day1(line) for line in self.input].count(True)
        print(f"Day 1: {number_of_nice}")
    def day_2(self):
        number_of_nice = [self.is_nice_day2(line) for line in self.input].count(True)
        print(f"Day 2: {number_of_nice}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

solver = script(input)
solver.day_1()
solver.day_2()