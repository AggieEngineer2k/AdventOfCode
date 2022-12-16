x = 1
registers = list()

def noop():
    global x,registers
    registers.append(x)
    return

def addx(value : int):
    global x,registers
    registers.append(x)
    registers.append(x)
    x += value
    return

lines = None
with open('input.txt','r') as inputFile:
    lines = [line.rstrip() for line in inputFile]
for line in lines:
    if line == 'noop':
        noop()
    elif line.startswith('addx'):
        addx(int(line.split()[1]))

# Part 1
strengths = 0
cycles = [20,60,100,140,180,220]
for cycle in cycles:
    strengths += cycle * registers[cycle - 1]
print(strengths)