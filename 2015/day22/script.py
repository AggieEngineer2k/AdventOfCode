import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARNING)

class Combatant:
    hit_points : int
    mana : int
    damage : int
    def __init__(self, hit_points : int = 0, mana : int = 0, damage : int = 0):
        self.hit_points = hit_points
        self.mana = mana
        self.damage = damage
    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Combatant):
            return NotImplemented
        return (self is other) or (self.hit_points == other.hit_points and self.mana == other.mana and self.damage == other.damage)
    def __str__(self) -> str:
        return f"(HP:{self.hit_points}/M:{self.mana}/D:{self.damage})"
    __repr__ = __str__

class Script:
    player : Combatant
    boss : Combatant
    def __init__(self, input : "list[str]" = [], player_hit_points : int = 50, player_mana : int = 500):
        self.player = Combatant(hit_points=player_hit_points, mana=player_mana)
        self.boss = Combatant(hit_points=int(input[0].replace("Hit Points: ","")),damage=int(input[1].replace("Damage: ","")))
    def day_1(self):
        print(f"Day 1: ")
    def day_2(self):
        print(f"Day 2: ")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1()
script.day_2()