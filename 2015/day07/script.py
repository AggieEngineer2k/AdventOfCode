import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARN)
import re

class Script:
    def get_dictionary_key_value_from_instruction(self, instruction : str):
        if re.search("^\d+ -> [a-z]+$", instruction):
            # 123 -> x
            # 456 -> y
            result = re.search("(\d+) -> ([a-z]+)", instruction)
            return {result.group(2) : int(result.group(1))}
        elif re.search("^[a-z]+ AND [a-z]+ -> [a-z]+$", instruction):
            # x AND y -> d
            result = re.search("([a-z]+) AND ([a-z]+) -> ([a-z]+)", instruction)
            return {result.group(3) : f"{result.group(1)} & {result.group(2)}"}
        elif re.search("^[a-z]+ OR [a-z]+ -> [a-z]+$", instruction):
            # x OR y -> e
            result = re.search("([a-z]+) OR ([a-z]+) -> ([a-z]+)", instruction)
            return {result.group(3) : f"{result.group(1)} | {result.group(2)}"}
        elif re.search("^[a-z]+ LSHIFT \d+ -> [a-z]+$", instruction):
            # x LSHIFT 2 -> f
            result = re.search("([a-z]+) LSHIFT (\d+) -> ([a-z]+)", instruction)
            return {result.group(3) : f"{result.group(1)} << {result.group(2)}"}
        elif re.search("^[a-z]+ RSHIFT \d+ -> [a-z]+$", instruction):
            # y RSHIFT 2 -> g
            result = re.search("([a-z]+) RSHIFT (\d+) -> ([a-z]+)", instruction)
            return {result.group(3) : f"{result.group(1)} >> {result.group(2)}"}
        elif re.search("^NOT [a-z]+ -> [a-z]+$", instruction):
            # NOT x -> h
            # NOT y -> i
            result = re.search("NOT ([a-z]+) -> ([a-z]+)", instruction)
            return {result.group(2) : f"~{result.group(1)}"}
        elif re.search("^\d+ AND [a-z]+ -> [a-z]+$", instruction):
            # 1 AND x -> y
            result = re.search("(\d+) AND ([a-z]+) -> ([a-z]+)", instruction)
            return {result.group(3) : f"{result.group(1)} & {result.group(2)}"}
        elif re.search("^[a-z]+ -> [a-z]+$", instruction):
            # x -> y
            result = re.search("([a-z]+) -> ([a-z]+)", instruction)
            return {result.group(2) : result.group(1)}
    def get_value_for_dictionary_key(self, dictionary : dict, key : str) -> int:
        # 123
        # 456
        if isinstance(dictionary[key],int):
            return dictionary[key]
        # x
        elif re.search("^[a-z]+$", dictionary[key]):
            result = re.search("([a-z]+)", dictionary[key])
            dictionary[key] = self.get_value_for_dictionary_key(dictionary, result.group(1))
            return dictionary[key]
        # ~x
        # ~y
        elif re.search("^~[a-z]+$", dictionary[key]):
            result = re.search("~([a-z]+)", dictionary[key])
            dictionary[key] = ~self.get_value_for_dictionary_key(dictionary, result.group(1)) + 2**16
            return dictionary[key]
        # 1 & x
        elif re.search("^\d+ & [a-z]+$", dictionary[key]):
            result = re.search("(\d+) & ([a-z]+)", dictionary[key])
            dictionary[key] = int(result.group(1)) & self.get_value_for_dictionary_key(dictionary, result.group(2))
            return dictionary[key]
        # x & y
        elif re.search("^[a-z]+ & [a-z]+$", dictionary[key]):
            result = re.search("([a-z]+) & ([a-z]+)", dictionary[key])
            dictionary[key] = self.get_value_for_dictionary_key(dictionary, result.group(1)) & self.get_value_for_dictionary_key(dictionary, result.group(2))
            return dictionary[key]
        # x | y
        elif re.search("^[a-z]+ \\| [a-z]+$", dictionary[key]):
            result = re.search("([a-z]+) \\| ([a-z]+)", dictionary[key])
            dictionary[key] = self.get_value_for_dictionary_key(dictionary, result.group(1)) | self.get_value_for_dictionary_key(dictionary, result.group(2))
            return dictionary[key]
        # x << 2
        elif re.search("^[a-z]+ << \d+$", dictionary[key]):
            result = re.search("([a-z]+) << (\d+)", dictionary[key])
            dictionary[key] = self.get_value_for_dictionary_key(dictionary, result.group(1)) << int(result.group(2))
            return dictionary[key]
        # y >> 2
        elif re.search("^[a-z]+ >> \d+$", dictionary[key]):
            result = re.search("([a-z]+) >> (\d+)", dictionary[key])
            dictionary[key] = self.get_value_for_dictionary_key(dictionary, result.group(1)) >> int(result.group(2))
            return dictionary[key]
    def __init__(self, input : "list[str]" = []):
        self.input = input
    def day_1(self) -> int:
        dictionary = {}
        for instruction in self.input:
            dictionary.update(self.get_dictionary_key_value_from_instruction(instruction))
        a = self.get_value_for_dictionary_key(dictionary, "a")
        print(f"Day 1: {a}")
        return a
    def day_2(self, day_1 : int):
        dictionary = {}
        instructions = self.input
        instructions.append(f"{day_1} -> b")
        for instruction in instructions:
            dictionary.update(self.get_dictionary_key_value_from_instruction(instruction))
        a = self.get_value_for_dictionary_key(dictionary, "a")
        print(f"Day 2: {a}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
day_1 = script.day_1()
script.day_2(day_1)