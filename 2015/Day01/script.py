import os

class script:
    def floor_change(self, instruction : str):
        if instruction == "(":
            return 1
        elif instruction == ")":
            return -1
    def determine_floor(self, instructions : str):
        value = 0
        for instruction in instructions:
            value += self.floor_change(instruction)
        return value
    def determine_instruction_that_enters_basement(self, instructions : str):
        value = 0
        for i in range(0,len(instructions)):
            value += self.floor_change(instructions[i])
            if value < 0:
                return i + 1
            i += 1
    def __init__(self, input : str = ""):
        self.input = input
        pass
    def day_1(self):
        floor = self.determine_floor(self.input)
        print(f"Day 1: {floor}")
    def day_2(self):
        floor = self.determine_instruction_that_enters_basement(self.input)
        print(f"Day 2: {floor}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
with open(input_path,'r') as inputFile:
    line = inputFile.read().strip()

solver = script(line)
solver.day_1()
solver.day_2()