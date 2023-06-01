import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARNING)
import re
from common.graph import Graph

class Script:
    input : "list[str]"
    replacements : dict
    medicine : "list[str]"
    def parse_input(self, input : "list[str]" = []) -> tuple:
        graph = Graph()
        medicine = ""
        for line in input:
            if re.match(r"\w+ => \w+", line):
                results = re.search(r"(\w+) => (\w+)", line)
                graph.add_edge(results.group(1), results.group(2), 0, symmetric=False)
            elif re.match(r"\w+", line):
                medicine = line
        replacements = dict(map(lambda x: (x[0],list(x[1].keys())), graph.dictionary.items()))
        return (replacements, medicine)
    def __init__(self, input : "list[str]" = []):
        self.input = input
        results = self.parse_input(self.input)
        self.replacements = results[0]
        self.medicine = self.split_medicine(results[1])
    def split_medicine(self, medicine : str) -> "list[str]":
        return re.findall(r"([A-Z][a-z]?)", medicine)
    def generate_one_off_molecules(self, medicine : "list[str]", replacements : dict) -> set:
        molecules = set()
        for i in range(len(medicine)):
            if medicine[i] in replacements.keys():
                for replacement in replacements[medicine[i]]:
                    new_molecule = ''.join(medicine[:i]) + replacement + ''.join(medicine[i+1:])
                    logging.debug(f"{i:3} {new_molecule}")
                    molecules.add(new_molecule)
            else:
                logging.debug(f"{i:3} {''.join(medicine[:i]) + '_' + medicine[i] + '_' + ''.join(medicine[i+1:])}")
        return molecules
    def generate_all_molecules(self, medicine : "list[str]", replacements : dict, molecules : set, molecule : str = "", index : int = 0):
        element = medicine[index]
        for replacement in [element] + replacements[element]:
            new_molecule = molecule + replacement
            if index == len(medicine) - 1:
                molecules.add(new_molecule)
            else:
                self.generate_all_molecules(medicine, replacements, molecules, new_molecule, index + 1)
    def day_1(self):
        molecules = self.generate_one_off_molecules(self.medicine, self.replacements)
        print(f"Day 1: {len(molecules)}")
    def day_2(self):
        print(f"Day 2: ")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1()
script.day_2()