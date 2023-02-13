import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARN)
import re

class Script:
    def get_edge_from_text(self, text : str) -> list:
        result = re.search("(.+) to (.+) = (\d+)", text)
        from_node_name = result.group(1)
        to_node_name = result.group(2)
        weight = int(result.group(3))
        return [from_node_name,to_node_name,weight]
    def add_edge_to_graph(self, graph : dict, from_node_name : str, to_node_name : str, weight : int):
        from_node_weights = graph.setdefault(from_node_name, {})
        from_node_weights.setdefault(to_node_name, weight)
        to_node_weights = graph.setdefault(to_node_name, {})
        to_node_weights.setdefault(from_node_name, weight)
    def get_graph_for_input(self, input : "list[str]") -> dict:
        dictionary = {}
        for line in input:
            edge = self.get_edge_from_text(line)
            self.add_edge_to_graph(dictionary, edge[0], edge[1], edge[2])
        return dictionary
    def __init__(self, input : "list[str]" = []):
        self.input = input
    def day_1(self):
        graph = self.get_graph_for_input(self.input)
        print(f"Day 1: ")
    def day_2(self):
        print(f"Day 2: ")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1()
script.day_2()