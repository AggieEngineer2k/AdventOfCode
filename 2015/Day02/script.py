import os
import re

class Present:
    def __init__(self, l : int, w : int, h : int):
        self.l = int(l)
        self.w = int(w)
        self.h = int(h)
    def __eq__(self, other):
        if self is other:
            return True
        elif isinstance(other, Present):
            return self.l == other.l and self.w == other.w and self.h == other.h
        else:
            return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def get_square_feet(self):
        lw = self.l * self.w
        wh = self.w * self.h
        hl = self.h * self.l
        largest_face = min(lw,wh,hl)
        return (2 * lw) + (2 * wh) + (2 * hl) + largest_face
    def get_ribbon_length(self):
        lw = (2 * self.l) + (2 * self.w)
        wh = (2 * self.w) + (2 * self.h)
        hl = (2 * self.h) + (2 * self.l)
        smallest_perimeter = min(lw,wh,hl)
        volume = self.l * self.w * self.h
        return smallest_perimeter + volume
        
class script:
    def __init__(self, input : "list[str]" = []):
        self.input = input
    def get_Present_from_dimensions(self, dimensions : str) -> Present:
        matches = re.match('(\d*)x(\d*)x(\d*)',dimensions)
        return Present(matches.group(1),matches.group(2),matches.group(3))
    def day_1(self):
        total_square_feet = sum([self.get_Present_from_dimensions(d).get_square_feet() for d in self.input])
        print(f"Day 1: {total_square_feet}")
    def day_2(self):
        total_ribbon_length = sum([self.get_Present_from_dimensions(d).get_ribbon_length() for d in self.input])
        print(f"Day 2: {total_ribbon_length}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
with open(input_path,'r') as inputFile:
    lines = [line.rstrip() for line in inputFile]

solver = script(lines)
solver.day_1()
solver.day_2()