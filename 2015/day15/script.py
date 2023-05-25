import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARNING)
import re

class Ingredient:
    name : str
    capacity : int
    durability : int
    flavor : int
    texture : int
    calories : int
    def __init__(self, name : str = "", capacity : int = 0, durability : int = 0, flavor : int = 0, texture : int = 0, calories : int = 0, input : str = ""):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories
        regex = r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"
        if re.match(regex, input):
            result = re.search(regex, input)
            self.name = result.group(1)
            self.capacity = int(result.group(2))
            self.durability = int(result.group(3))
            self.flavor = int(result.group(4))
            self.texture = int(result.group(5))
            self.calories = int(result.group(6))
    def __eq__(self, other): 
        if not isinstance(other, Ingredient):
            return NotImplemented
        return self.name == other.name \
            and self.capacity == other.capacity \
            and self.durability == other.durability \
            and self.flavor == other.flavor \
            and self.texture == other.texture \
            and self.calories == other.calories
    def __str__(self) -> str:
        return f"{self.name}: capacity {self.capacity}, durability {self.self}, flavor {self.flavor}, texture {self.texture}, calories {self.calories}"

class Script:
    def generate_addends(self, sum : int) -> "list[int]":
        return [[a,b,c,d] for a in range(sum+1) for b in range(sum+1) for c in range(sum+1) for d in range(sum+1) if a+b+c+d == sum]
    def calculate_score(self, amounts : "list[int]", ingredients : "list[Ingredient]"):
        capacity = max(0,sum([amounts[x] * ingredients[x].capacity for x in range(len(amounts))]))
        durability = max(0,sum([amounts[x] * ingredients[x].durability for x in range(len(amounts))]))
        flavor = max(0,sum([amounts[x] * ingredients[x].flavor for x in range(len(amounts))]))
        texture = max(0,sum([amounts[x] * ingredients[x].texture for x in range(len(amounts))]))
        return capacity * durability * flavor * texture
    def calculate_calories(self, amounts : "list[int]", ingredients : "list[Ingredient]"):
        calories = max(0,sum([amounts[x] * ingredients[x].calories for x in range(len(amounts))]))
        return calories
    def __init__(self, input : "list[str]" = []):
        self.input = input
    def day_1(self):
        all_amounts = self.generate_addends(100)
        ingredients = [Ingredient(input = line) for line in self.input]
        max_score = 0
        for amounts in all_amounts:
            max_score = max(max_score, self.calculate_score(amounts, ingredients))
        print(f"Day 1: {max_score}")
    def day_2(self):
        all_amounts = self.generate_addends(100)
        ingredients = [Ingredient(input = line) for line in self.input]
        max_score = 0
        for amounts in all_amounts:
            score = self.calculate_score(amounts, ingredients)
            calories = self.calculate_calories(amounts, ingredients)
            if calories == 500:
                max_score = max(max_score, score)
        print(f"Day 2: {max_score}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1()
script.day_2()