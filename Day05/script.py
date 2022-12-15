import re

stacks = [
    #         [C] [B] [H]                
    # [W]     [D] [J] [Q] [B]            
    # [P] [F] [Z] [F] [B] [L]            
    # [G] [Z] [N] [P] [J] [S] [V]        
    # [Z] [C] [H] [Z] [G] [T] [Z]     [C]
    # [V] [B] [M] [M] [C] [Q] [C] [G] [H]
    # [S] [V] [L] [D] [F] [F] [G] [L] [F]
    # [B] [J] [V] [L] [V] [G] [L] [N] [J]
    #  1   2   3   4   5   6   7   8   9 
    list(['B','S','V','Z','G','P','W']), #1
    list(['J','V','B','C','Z','F']), #2
    list(['V','L','M','H','N','Z','D','C']), #3
    list(['L','D','M','Z','P','F','J','B']), #4
    list(['V','F','C','G','J','B','Q','H']), #5
    list(['G','F','Q','T','S','L','B']), #6
    list(['L','G','C','Z','V']), #7
    list(['N','L','G']), #8
    list(['J','F','H','C']) #9
]

def extractCommands(line):
    regex = "[0-9]+"
    return [int(i) for i in re.findall(regex,str(line))]

def move(containers,fromstack,tostack):
    for i in range(0,containers):
        stacks[tostack - 1].append(stacks[fromstack - 1].pop())

lines = list()
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

for line in lines:
    commands = extractCommands(line)
    move(commands[0],commands[1],commands[2])

top_containers = ""
for stack in stacks:
    top_containers += stack[len(stack) - 1]

print(top_containers)