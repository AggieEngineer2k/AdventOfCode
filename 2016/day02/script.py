import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir))
from common.input_parser import InputParser
import logging
logging.basicConfig(level=logging.WARNING)

EDGE = '-'

class Keypad:
    buttons : "list(list(str))"
    row : int
    column : int
    def __init__(self, buttons : "list(list(str))", row : int, column : int):
        self.buttons = buttons
        self.row = row
        self.column = column
    def move(self, direction : str):
        if direction == 'U':
            self.row = max(0, self.row - 1)
            # if self.getButton() == EDGE:
            #     self.row = self.row + 1
        elif direction == 'D':
            self.row = min(2, self.row + 1)
            # if self.getButton() == EDGE:
            #     self.row = self.row - 1
        elif direction == 'L':
            self.column = max(0, self.column - 1)
            # if self.getButton() == EDGE:
            #     self.row = self.column + 1
        elif direction == 'R':
            self.column = min(2, self.column + 1)
            # if self.getButton() == EDGE:
            #     self.row = self.column - 1
    def getButton(self) -> str :
        return self.buttons[self.row][self.column]
    def getCode(self, instructions : "list(list(str))"):
        code = ""
        for line in instructions:
            for character in line:
                self.move(character)
            code = code + self.getButton()
        return code

class Script:
    input : "list(str)"
    def __init__(self, input : str = []):
        self.input = input
    def day_1(self):
        buttons = [
            ["1","2","3"],
            ["4","5","6"],
            ["7","8","9"]
        ]
        keypad = Keypad(buttons,1,1)
        code = keypad.getCode(self.input)
        print(f"Day 1: {code}")
    def day_2(self):
        buttons = [
            [EDGE, EDGE, "1", EDGE, EDGE],
            [EDGE, "2",  "3", "4",  EDGE],
            ["5",  "6",  "7", "8",  "9"],
            [EDGE, "A",  "B", "C",  EDGE],
            [EDGE, EDGE, "D", EDGE, EDGE]
        ]
        keypad = Keypad(buttons,2,0)
        code = keypad.getCode(self.input)
        print(f"Day 2: {code}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
input = InputParser.parse_lines(input_path)

script = Script(input)
script.day_1()
script.day_2()