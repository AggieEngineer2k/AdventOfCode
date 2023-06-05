import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARNING)
import itertools,re,math

class Item:
    name : str
    cost : int
    damage : int
    armor : int
    def __init__(self, name : str, cost : int, damage : int, armor : int):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor
    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Item):
            return NotImplemented
        return self.name == other.name and self.cost == other.cost and self.damage == other.damage and self.armor == other.armor
    def __str__(self) -> str:
        return f"{self.name} ({self.cost}/{self.damage}/{self.armor})"
    __repr__ = __str__

class Combatant:
    hit_points : int
    damage : int
    armor : int
    cost : int
    def __init__(self, hit_points : int, damage : int, armor : int, cost : int = 0):
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor
        self.cost = cost
    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Combatant):
            return NotImplemented
        return self.hit_points == other.hit_points and self.damage == other.damage and self.armor == other.armor and self.cost == other.cost
    def __str__(self) -> str:
        return f"({self.hit_points}/{self.damage}/{self.armor}/{self.cost})"
    __repr__ = __str__
    def wins_against(self, opponent : 'Combatant'):
        combatant_damages_for = max(self.damage - opponent.armor,1)
        opponent_damages_for = max(opponent.damage - self.armor,1)
        combatant_turns = math.ceil(opponent.hit_points / combatant_damages_for)
        opponent_turns = math.ceil(self.hit_points / opponent_damages_for)
        is_win = combatant_turns <= opponent_turns
        log = f"{self} hits for {combatant_damages_for}, {opponent} hits for {opponent_damages_for}."
        if is_win:
            logging.debug(f"{log} wins in {combatant_turns}.")
        else:
            logging.debug(f"{log} looses in {opponent_turns}.")
        return is_win

Weapons = [
    Item('Dagger',8,4,0),
    Item('Shortsword',10,5,0),
    Item('Warhammer',25,6,0),
    Item('Longsword',40,7,0),
    Item('Greataxe',74,8,0),
]
Armors = [
    None,
    Item('Leather',13,0,1),
    Item('Chainmail',31,0,2),
    Item('Splintmail',53,0,3),
    Item('Bandedmail',75,0,4),
    Item('Platemail',102,0,5),
]
Rings = [
    None,
    Item('Damage +1',25,1,0),
    Item('Damage +2',50,2,0),
    Item('Damage +3',100,3,0),
    Item('Defense +1',20,0,1),
    Item('Defense +2',40,0,2),
    Item('Defense +3',80,0,3),
]

class Script:
    input : int
    boss : Combatant
    def __init__(self, input : "list[str]" = []):
        self.input = input
    def parse_input(self, input : "list[str]"):
        hit_points = 0
        damage = 0
        armor = 0
        for line in input:
            split = re.split(r"\s",line)
            if split[0] == "Hit":
                hit_points = int(split[2])
            elif split[0] == "Damage:":
                damage = int(split[1])
            elif split[0] == "Armor:":
                armor = int(split[1])
        return Combatant(hit_points,damage,armor)
    def get_inventories(self):
        return [
            {
                'weapon':x[0],
                'armor':x[1],
                'ring1':x[2],
                'ring2':x[3],
                'cost':sum(y.cost for y in x if hasattr(y,'cost')),
                '+damage':sum(y.damage for y in x if hasattr(y,'damage')),
                '+armor':sum(y.armor for y in x if hasattr(y,'armor')),
            } for x in itertools.product(*[Weapons,Armors,Rings,Rings])
            if x[2] != x[3]
            and not (x[2] is None and x[3] is not None)
        ]
    def day_1(self):
        inventories = self.get_inventories()
        players = [Combatant(100,i['+damage'],i['+armor'],i['cost']) for i in inventories]
        winners = [p for p in players if p.wins_against(self.boss)]
        winners = sorted(winners, key=lambda x: x.cost)
        print(f"Day 1: {winners[0].cost}")
    def day_2(self):
        inventories = self.get_inventories()
        players = [Combatant(100,i['+damage'],i['+armor'],i['cost']) for i in inventories]
        lossers = [p for p in players if not p.wins_against(self.boss)]
        loosers = sorted(lossers, key=lambda x: x.cost, reverse=True)
        print(f"Day 2: {loosers[0].cost}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.boss = script.parse_input(script.input)
script.day_1()
script.day_2()