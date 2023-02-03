import logging
logging.basicConfig(level=logging.WARN)
import os
import hashlib

class script:
    def __init__(self, input : str = ""):
        self.input = input
    def get_hash_hexdigest(self, key : str, number : int) -> str:
        return hashlib.md5(f"{key}{number}".encode()).hexdigest()
    def day_1(self):
        for i in range(100000,999999):
            if self.get_hash_hexdigest(self.input, i).startswith("000000"):
                break
        print(f"Day 1: {i}")
    def day_2(self):
        print(f"Day 2: ")

input_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),'input.txt'))
with open(input_path,'r') as inputFile:
    line = inputFile.readline().strip()

solver = script(line)
solver.day_1()
solver.day_2()