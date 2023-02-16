import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARN)
import re
from common.graph import Graph

class Script:
    def get_edge_from_text(self, text : str) -> list:
        result = re.search("(.+) to (.+) = (\d+)", text)
        from_node_name = result.group(1)
        to_node_name = result.group(2)
        weight = int(result.group(3))
        return [from_node_name,to_node_name,weight]
    def get_graph_for_input(self, input : "list[str]") -> Graph:
        graph = Graph()
        for line in input:
            edge = self.get_edge_from_text(line)
            graph.add_edge(edge[0], edge[1], edge[2])
        return graph
    def __init__(self, input : "list[str]" = []):
        self.input = input
    def day_1(self, graph : Graph):
        traveling_salesman = graph.get_traveling_salesman_shortest()
        print(f"Day 1: {traveling_salesman[0]}")
    def day_2(self, graph : Graph):
        traveling_salesman = graph.get_traveling_salesman_longest()
        print(f"Day 2: {traveling_salesman[0]}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
graph = script.get_graph_for_input(script.input)
script.day_1(graph)
script.day_2(graph)