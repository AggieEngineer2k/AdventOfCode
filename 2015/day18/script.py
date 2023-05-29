import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARNING)

class Script:
    lights : "list[list[bool]]"
    def __init__(self, input : "list[str]" = []):
        self.input = input
    def parse_input(self, input : "list[str]" = []) -> "list[list[bool]]":
        array = [[None for c in range(len(input[0]))] for r in range(len(input))]
        for row in range(len(input)):
            for col in range(len(input[0])):
                array[row][col] = input[row][col] == '#'
        return array
    def get_neighbor_indexes(self, row : int, column : int, height : int, width : int) -> "list[tuple]":
        neighbor_indexes = []
        neighbor_indexes.append((row-1,column-1))
        neighbor_indexes.append((row-1,column))
        neighbor_indexes.append((row-1,column+1))
        neighbor_indexes.append((row,column-1))
        neighbor_indexes.append((row,column+1))
        neighbor_indexes.append((row+1,column-1))
        neighbor_indexes.append((row+1,column))
        neighbor_indexes.append((row+1,column+1))
        return [neighbor_index for neighbor_index in neighbor_indexes
            if neighbor_index[0] >= 0
            and neighbor_index[0] < height
            and neighbor_index[1] >= 0
            and neighbor_index[1] < width
        ]
    def get_neighbor_values(self, row : int, column : int, array : "list[list[bool]]") -> "list[bool]":
        neighbor_indexes = self.get_neighbor_indexes(row=row, column=column, height=len(array), width=len(array[0]))
        return [array[neighbor_index[0]][neighbor_index[1]] for neighbor_index in neighbor_indexes]
    def get_new_state(self, current_state : bool, neighbors : "list[bool]") -> bool:
        neighbors_on = sum(1 for neighbor in neighbors if neighbor == True)
        if current_state == True:
            return neighbors_on in [2,3]
        else:
            return neighbors_on == 3
    def get_new_array(self, array : "list[list[bool]]", corners : bool = False) -> "list[list[bool]]":
        rows = len(array)
        colums = len(array[0])
        new_array = [[None for c in range(colums)] for r in range(rows)]
        for row in range(rows):
            for col in range(colums):
                neighbors = self.get_neighbor_values(row, col, array)
                new_array[row][col] = self.get_new_state(array[row][col], neighbors)
                if corners and ( \
                    (row == 0 and col == 0) \
                    or (row == rows-1 and col == 0) \
                    or (row == 0 and col == colums-1) \
                    or (row == rows-1 and col == colums-1)):
                    new_array[row][col] = True
        return new_array
    def day_1(self):
        array = self.parse_input(self.input)
        for i in range(100):
            array = self.get_new_array(array)
        lights_on = sum(1 for row in range(len(array)) for col in range(len(array[0])) if array[row][col] == True)
        print(f"Day 1: {lights_on}")
    def day_2(self):
        array = self.parse_input(self.input)
        for i in range(100):
            array = self.get_new_array(array, corners=True)
        lights_on = sum(1 for row in range(len(array)) for col in range(len(array[0])) if array[row][col] == True)
        print(f"Day 2: {lights_on}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1()
script.day_2()