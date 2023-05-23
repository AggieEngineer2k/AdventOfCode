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
    points : int
    distance : int
    def __init__(self, name : str = "", speed_km_s : int = 0, fly_s : int = 0, rest_s : int = 0, input : str = ""):
        self.name = name
        self.speed_km_s = speed_km_s
        self.fly_s = fly_s
        self.rest_s = rest_s
        self.points = 0
        self.distance = 0
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
    def __str__(self) -> str:
        return f"{self.name} has {self.points} points after traveling {self.distance} km."
    
class Race:
    def __init__(self, input : "list[str]" = []):
        self.racers = dict()
        for line in input:
            reindeer = Reindeer(input = line)
            self.racers[reindeer.name] = reindeer
    def run_race(self, time_s : int):
        racer : Reindeer
        # Initialize race to starting line.
        for name in self.racers:
            self.racers[name].points = 0
            self.racers[name].distance = 0
        # Run the race one second at a time.
        for i in range(1,time_s + 1):
            logging.debug(f"=== {i} s ===")
            for name in self.racers:
                racer = self.racers[name]
                racer.distance = racer.distance_traveled(i)
                logging.debug(f"{racer.name} has traveled {racer.distance} km.")
            max_distance = max([self.racers[name].distance for name in self.racers])
            logging.debug(f"Leaders are at {max_distance} km.")
            for name in self.racers:
                racer = self.racers[name]
                if(racer.distance == max_distance):
                   racer.points += 1
                   logging.debug(f"{racer.name} now has {racer.points} points.")
    def get_point_winners(self) -> "list[Reindeer]":
        max_points = max([self.racers[name].points for name in self.racers])
        return [self.racers[name] for name in self.racers if self.racers[name].points == max_points]

class Script:
    def __init__(self, input : "list[str]" = []):
        self.input = input
    def day_1(self, time : int):
        distances = []
        for line in self.input:
            reindeer = Reindeer(input = line)
            distances.append(reindeer.distance_traveled(time))
        max_distance = max(distances)
        print(f"Day 1: {max_distance}")
    def day_2(self, time : int):
        race = Race(self.input)
        race.run_race(time)
        winners = race.get_point_winners()
        print(f"Day 2: {winners[0].points}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1(2503)
script.day_2(2503)