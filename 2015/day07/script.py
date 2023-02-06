import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARN)
import re

class Script:
    def get_code_from_instruction(self, instruction : str) -> str:
        if re.search("^\d+ -> [a-z]+$", instruction):
            # 123 -> x
            # 456 -> y
            result = re.search("(\d+) -> ([a-z]+)", instruction)
            return f"def _{result.group(2)}() : return {result.group(1)}"
        elif re.search("^[a-z]+ AND [a-z]+ -> [a-z]+$", instruction):
            # x AND y -> d
            result = re.search("([a-z]+) AND ([a-z]+) -> ([a-z]+)", instruction)
            return f"def _{result.group(3)}() : return _{result.group(1)}() & _{result.group(2)}()"
        elif re.search("^[a-z]+ OR [a-z]+ -> [a-z]+$", instruction):
            # x OR y -> e
            result = re.search("([a-z]+) OR ([a-z]+) -> ([a-z]+)", instruction)
            return f"def _{result.group(3)}() : return _{result.group(1)}() | _{result.group(2)}()"
        elif re.search("^[a-z]+ LSHIFT \d+ -> [a-z]+$", instruction):
            # x LSHIFT 2 -> f
            result = re.search("([a-z]+) LSHIFT (\d+) -> ([a-z]+)", instruction)
            return f"def _{result.group(3)}() : return _{result.group(1)}() << {result.group(2)}"
        elif re.search("^[a-z]+ RSHIFT \d+ -> [a-z]+$", instruction):
            # y RSHIFT 2 -> g
            result = re.search("([a-z]+) RSHIFT (\d+) -> ([a-z]+)", instruction)
            return f"def _{result.group(3)}() : return _{result.group(1)}() >> {result.group(2)}"
        elif re.search("^NOT [a-z]+ -> [a-z]+$", instruction):
            # NOT x -> h
            # NOT y -> i
            result = re.search("NOT ([a-z]+) -> ([a-z]+)", instruction)
            return f"def _{result.group(2)}() : return ~_{result.group(1)}() + 2**16"
        elif re.search("^\d+ AND [a-z]+ -> [a-z]+$", instruction):
            # 1 AND x -> y
            result = re.search("(\d+) AND ([a-z]+) -> ([a-z]+)", instruction)
            return f"def _{result.group(3)}() : return {result.group(1)} & _{result.group(2)}()"
        elif re.search("^[a-z]+ -> [a-z]+$", instruction):
            # x -> y
            result = re.search("([a-z]+) -> ([a-z]+)", instruction)
            return f"def _{result.group(2)}() : return _{result.group(1)}()"
    def __init__(self, input : "list[str]" = []):
        self.input = input
    def day_1(self):
        for instruction in self.input:
            code = self.get_code_from_instruction(instruction)
            logging.debug(f"{instruction} => {code}")
            exec(code,globals())
        local = {}
        exec("signal = _a()",globals(),local)
        print(f"Day 1: {local['signal']}")
    def day_2(self):
        print(f"Day 2: ")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1()
script.day_2()