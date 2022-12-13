def getOutcome(opponent,you):
    loss = 0
    draw = 3
    win = 6
    if opponent == 'A': # Rock
        if you == 'X': # Rock
            return draw
        elif you == 'Y': # Paper
            return win
        elif you == 'Z': # Scissor
            return loss
    elif opponent == 'B': # Paper
        if you == 'X': # Rock
            return loss
        elif you == 'Y': # Paper
            return draw
        elif you == 'Z': # Scissor
            return win
    elif opponent == 'C': # Scissor
        if you == 'X': # Rock
            return win
        elif you == 'Y': # Paper
            return loss
        elif you == 'Z': # Scissor
            return draw

def score(opponent,you):
    if you == 'X': # Rock
        return getOutcome(opponent,you) + 1
    elif you == 'Y': # Paper
        return getOutcome(opponent,you) + 2
    elif you == 'Z': # Scissor
        return getOutcome(opponent,you) + 3
    
total = 0
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        play = line.strip().split()
        total += score(play[0],play[1])

print(total)