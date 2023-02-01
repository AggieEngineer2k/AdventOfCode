import os
import re

class Present:
    def __init__(self, l : int, w : int, h : int):
        self.l = int(l)
        self.w = int(w)
        self.h = int(h)
    def __eq__(self, other):
        if isinstance(other, Present):
            return self.l == other.l and self.w == other.w and self.h == other.h
        return False
    def __ne__(self, other):
        return not self.__eq__(other)

class script:
    def __init__(self, input : "list[str]" = []):
        self.input = input
    def get_Present_from_dimensions(self, dimensions : str) -> Present:
        dimension_array = re.findall('\d',dimensions)
        return Present(dimension_array[0],dimension_array[1],dimension_array[2])
    def get_present_square_feet(self, present: Present):
        pass
    def day_1(self):
        print(f"Day 1: ")
    def day_2(self):
        print(f"Day 2: ")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
with open(input_path,'r') as inputFile:
    lines = [line.rstrip() for line in inputFile]

solver = script(lines)
solver.day_1()
solver.day_2()