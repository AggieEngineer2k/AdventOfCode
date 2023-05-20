import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARNING)
import re
from common.graph import Graph
from itertools import permutations

class Script:
    def add_host(self, graph : Graph) -> Graph:
        for guest in list(graph.dictionary.keys()):
            graph.add_edge('host', guest, 0, symmetric=True)
        return graph
    def max_happiness(self, graph : Graph) -> int:
        guests = list(graph.dictionary.keys())
        happiness = 0
        # Remove redundant cyclic rotations ("necklaces"?) by popping off an element before permutating, and pushing back on to the permutations later.
        for permutation in [list(i) for i in permutations(guests[1:])]:
            permutation.append(guests[0])
            happiness = max(happiness, self.total_happiness(permutation, graph))
        return happiness
    def total_happiness(self, seating_arrangement : "list[str]", graph : Graph) -> int:
        happiness = 0
        number_of_guests = len(seating_arrangement)
        # First guest
        happiness += graph.get_edge_weight(seating_arrangement[0],seating_arrangement[number_of_guests-1])
        happiness += graph.get_edge_weight(seating_arrangement[0],seating_arrangement[1])
        # Last guest
        happiness += graph.get_edge_weight(seating_arrangement[number_of_guests-1],seating_arrangement[number_of_guests-2])
        happiness += graph.get_edge_weight(seating_arrangement[number_of_guests-1],seating_arrangement[0])
        # All other guests
        for i in range(1,number_of_guests-1):
            happiness += graph.get_edge_weight(seating_arrangement[i],seating_arrangement[i-1])
            happiness += graph.get_edge_weight(seating_arrangement[i],seating_arrangement[i+1])
        return happiness
    def build_graph(self, input : "list[str]") -> Graph:
        graph = Graph()
        for line in input:
            edge = self.parse_edge(line)
            graph.add_edge(from_node_name=edge[0], to_node_name=edge[1], weight=edge[2], symmetric=False)
        return graph
    def parse_edge(self, input : str) -> tuple:
        m = re.match(r"(?P<guest>\w+) would (?P<change>\w+) (?P<amount>\d+) happiness units by sitting next to (?P<neighbor>\w+).", input)
        return (m.group('guest'), m.group('neighbor'), int(m.group('amount')) if m.group('change') == 'gain' else -int(m.group('amount')))
    def __init__(self, input : "list[str]" = []):
        self.input = input
    def day_1(self):
        graph = self.build_graph(self.input)
        max_happiness = self.max_happiness(graph)
        print(f"Day 1: {max_happiness}")
    def day_2(self):
        graph = self.build_graph(self.input)
        graph = self.add_host(graph)
        max_happiness = self.max_happiness(graph)
        print(f"Day 2: {max_happiness}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1()
script.day_2()