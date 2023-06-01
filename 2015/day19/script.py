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
    medicine : str
    formula : "list[str]"
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
        self.medicine = results[1]
        self.formula = self.split_medicine(self.medicine)
    def split_medicine(self, medicine : str) -> "list[str]":
        return re.findall(r"([e]|[A-Z][a-z]?)", medicine)
    def generate_one_off_molecules(self, formula : "list[str]", replacements : dict) -> set:
        molecules = set()
        for i in range(len(formula)):
            if formula[i] in replacements.keys():
                for replacement in replacements[formula[i]]:
                    #logging.debug(f"{i:3} {''.join(formula[:i]) + ' (' + formula[i] + '=>' + replacement + ') ' + ''.join(formula[i+1:])}")
                    new_molecule = ''.join(formula[:i]) + replacement + ''.join(formula[i+1:])
                    molecules.add(new_molecule)
            else:
                #logging.debug(f"{i:3} {''.join(formula[:i]) + ' (' + formula[i] + ') ' + ''.join(formula[i+1:])}")
                pass
        return molecules
    def generate_all_molecules(self, formula : "list[str]", replacements : dict, molecules : set, molecule : str = "", index : int = 0):
        element = formula[index]
        for replacement in [element] + replacements[element]:
            new_molecule = molecule + replacement
            if index == len(formula) - 1:
                molecules.add(new_molecule)
            else:
                self.generate_all_molecules(formula, replacements, molecules, new_molecule, index + 1)
    def day_1(self):
        molecules = self.generate_one_off_molecules(self.formula, self.replacements)
        print(f"Day 1: {len(molecules)}")
    def day_2(self):
        # This should be a function with a unit test.
        step = 0
        medicines = {'e'}
        new_medicines = set()
        while step < 50:
            logging.debug(f"Starting step {step + 1} on {len(medicines)} medicines.")
            new_medicines.clear()
            for medicine in medicines:
                logging.debug(f"Calculating new medicines from {medicine}.")
                formula = self.split_medicine(medicine)
                one_off_molecules = self.generate_one_off_molecules(formula, self.replacements)
                logging.debug(f"Calculated {len(one_off_molecules)} molecules: {one_off_molecules}")
                new_medicines.update(one_off_molecules)
            if self.medicine in new_medicines:
                break
            else:
                medicines = new_medicines.copy()
                step = step + 1
        print(f"Day 2: {step + 1}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1()
script.day_2()