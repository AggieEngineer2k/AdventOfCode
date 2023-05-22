import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARNING)
import re
from typing import NamedTuple

class Reindeer:
    name : str
    speed_km_s : int
    fly_s : int
    rest_s : int
    def __init__(self, name : str = "", speed_km_s : int = 0, fly_s : int = 0, rest_s : int = 0, input : str = ""):
        self.name = name
        self.speed_km_s = speed_km_s
        self.fly_s = fly_s
        self.rest_s = rest_s
        regex = r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
        if re.match(regex, input):
            result = re.search(regex, input)
            self.name = result.group(1)
            self.speed_km_s = int(result.group(2))
            self.fly_s = int(result.group(3))
            self.rest_s = int(result.group(4))
    def distance_traveled(self, time : int) -> int:
        cycle = self.fly_s + self.rest_s
        completions = time // cycle
        partials = time % cycle
        distance = ((self.fly_s * completions) + min(self.fly_s, partials)) * self.speed_km_s
        return distance
    def __eq__(self, other): 
        if not isinstance(other, Reindeer):
            return NotImplemented
        return self.name == other.name \
            and self.speed_km_s == other.speed_km_s \
            and self.fly_s == other.fly_s \
            and self.rest_s == other.rest_s

class Script:
    def __init__(self, input : "list[str]" = []):
        self.input = input
    def day_1(self, time : int):
        winner = 0
        for line in self.input:
            reindeer = Reindeer(input = line)
            distance = reindeer.distance_traveled(time)
            winner = max(winner, distance)
        print(f"Day 1: {winner}")
    def day_2(self):
        print(f"Day 2: ")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1(2503)
script.day_2()