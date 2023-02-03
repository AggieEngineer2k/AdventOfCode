import os

class InputParser:
    def parse_line(filepath : str) -> str:
        with open(filepath,'r') as file:
            return file.readline().strip()

    def parse_lines(filepath : str) -> "list[str]":
        with open(filepath,'r') as file:
            return [line.strip() for line in file.readlines()]