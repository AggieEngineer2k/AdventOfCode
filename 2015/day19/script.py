import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.DEBUG)
import re
from common.graph import Graph

class Script:
    input : "list[str]"
    replacements : dict
    reverse_replacements : dict
    medicine : str
    formula : "list[str]"
    def parse_input(self, input : "list[str]" = []) -> tuple:
        replacements_graph = Graph()
        reverse_replacements_graph = Graph()
        medicine = ""
        for line in input:
            if re.match(r"\w+ => \w+", line):
                results = re.search(r"(\w+) => (\w+)", line)
                replacements_graph.add_edge(results.group(1), results.group(2), 0, symmetric=False)
                reverse_replacements_graph.add_edge(results.group(2), results.group(1), 0, symmetric=False)
            elif re.match(r"\w+", line):
                medicine = line
        replacements = dict(map(lambda x: (x[0],list(x[1].keys())), replacements_graph.dictionary.items()))
        reverse_replacements = dict(map(lambda x: (x[0],list(x[1].keys())), reverse_replacements_graph.dictionary.items()))
        return (replacements, medicine, reverse_replacements)
    def __init__(self, input : "list[str]" = []):
        self.input = input
        results = self.parse_input(self.input)
        self.replacements = results[0]
        self.medicine = results[1]
        self.formula = self.split_medicine(self.medicine)
        self.reverse_replacements = results[2]
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
    # def generate_all_molecules(self, formula : "list[str]", replacements : dict, molecules : set, molecule : str = "", index : int = 0):
    #     element = formula[index]
    #     for replacement in [element] + replacements[element]:
    #         new_molecule = molecule + replacement
    #         if index == len(formula) - 1:
    #             molecules.add(new_molecule)
    #         else:
    #             self.generate_all_molecules(formula, replacements, molecules, new_molecule, index + 1)
    def generate_one_off_source_molecules(self, medicine : str, reverse_replacements : dict) -> set:
        source_medicines = set()
        for key,value in reverse_replacements.items():
            for replacement in value:
                occurrence_indexes = [match.start() for match in re.finditer(pattern=f"(?={key})", string=medicine)]
                for i in occurrence_indexes:
                    source_medicines.add(medicine[:i] + replacement + medicine[i+len(key):])
        return source_medicines
    def day_1(self):
        molecules = self.generate_one_off_molecules(self.formula, self.replacements)
        print(f"Day 1: {len(molecules)}")
    def day_2(self):
        step = 1
        medicine = self.medicine
        reverse_replacement_keys = sorted(self.reverse_replacements.keys(),key=len,reverse=True)
        while medicine != "e":
            logging.debug(f"Starting step {step} on {medicine}.")
            for key in reverse_replacement_keys:
                index = medicine.find(key)
                if index > -1:
                    source = self.reverse_replacements[key][0]
                    logging.debug(f"Replacing {key} with {source}.")
                    medicine = medicine[:index] + source + medicine[index + len(key):]
                    break
            if medicine == "e":
                break
            else:
                step = step + 1

        # Brute force reverse method.
        # step = 0
        # medicines = {self.medicine}
        # source_medicines = set()
        # while True:
        #     logging.debug(f"Starting step {step + 1} on {len(medicines)} medicines.")
        #     source_medicines.clear()
        #     for medicine in medicines:
        #         logging.debug(f"Calculating source medicines for {medicine}.")
        #         new_source_medicines = self.generate_one_off_source_molecules(medicine, self.reverse_replacements)
        #         logging.debug(f"Calculated {len(new_source_medicines)} medicines: {new_source_medicines}")
        #         source_medicines.update(new_source_medicines)
        #     if 'e' in source_medicines:
        #         break
        #     else:
        #         medicines = source_medicines.copy()
        #         step = step + 1

        # Brute force forward method.
        # step = 0
        # medicines = {'e'}
        # new_medicines = set()
        # while step < 50:
        #     logging.debug(f"Starting step {step + 1} on {len(medicines)} medicines.")
        #     new_medicines.clear()
        #     for medicine in medicines:
        #         logging.debug(f"Calculating new medicines from {medicine}.")
        #         formula = self.split_medicine(medicine)
        #         one_off_molecules = self.generate_one_off_molecules(formula, self.replacements)
        #         logging.debug(f"Calculated {len(one_off_molecules)} molecules: {one_off_molecules}")
        #         new_medicines.update(one_off_molecules)
        #     if self.medicine in new_medicines:
        #         break
        #     else:
        #         medicines = new_medicines.copy()
        #         step = step + 1
        print(f"Day 2: {step}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1()
script.day_2()