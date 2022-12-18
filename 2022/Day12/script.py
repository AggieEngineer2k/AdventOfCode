class Solver:
    def __init__(self, map) -> None:
        self.map = map
    def show(self):
        [print(''.join([str(c) for c in r])) for r in self.map]

solver : Solver
with open('input.txt','r') as inputFile:
    solver = Solver([list(line.rstrip()) for line in inputFile])

solver.show()