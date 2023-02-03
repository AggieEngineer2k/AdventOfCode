import logging
logging.basicConfig(level=logging.WARN)
import os
import hashlib

class script:
    def __init__(self, input : str = ""):
        self.input = input
    def get_hash_hexdigest(self, key : str, number : int) -> str:
        return hashlib.md5(f"{key}{number}".encode()).hexdigest()
    def find_number_for_hash_startswith(self, key : str, startswith : str):
        i = 1
        while i < 9999999:
            if self.get_hash_hexdigest(key, i).startswith(startswith):
                return i
            i += 1
    def day_1(self):
        number = self.find_number_for_hash_startswith(self.input, "0" * 5)
        print(f"Day 1: {number}")
    def day_2(self):
        number = self.find_number_for_hash_startswith(self.input, "0" * 6)
        print(f"Day 2: {number}")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
with open(input_path,'r') as inputFile:
    line = inputFile.readline().strip()

solver = script(line)
solver.day_1()
solver.day_2()