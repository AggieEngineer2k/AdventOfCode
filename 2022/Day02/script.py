opponent_rock = 'A'
opponent_paper = 'B'
opponent_scissor = 'C'

you_rock = 'X'
you_paper = 'Y'
you_scissor = 'Z'

you_lose = 'X'
you_draw = 'Y'
you_win = 'Z'

def getOutcome(opponent,you):
    loss = 0
    draw = 3
    win = 6
    if opponent == opponent_rock:
        if you == you_rock:
            return draw
        elif you == you_paper:
            return win
        elif you == you_scissor:
            return loss
    elif opponent == opponent_paper:
        if you == you_rock:
            return loss
        elif you == you_paper:
            return draw
        elif you == you_scissor:
            return win
    elif opponent == opponent_scissor:
        if you == you_rock:
            return win
        elif you == you_paper:
            return loss
        elif you == you_scissor:
            return draw

def lose(opponent):
    if opponent == opponent_rock:
        return you_scissor
    elif opponent == opponent_paper:
        return you_rock
    elif opponent == opponent_scissor:
        return you_paper

def draw(opponent):
    if opponent == opponent_rock:
        return you_rock
    elif opponent == opponent_paper:
        return you_paper
    elif opponent == opponent_scissor:
        return you_scissor

def win(opponent):
    if opponent == opponent_rock:
        return you_paper
    elif opponent == opponent_paper:
        return you_scissor
    elif opponent == opponent_scissor:
        return you_rock

def score(opponent,you):
    outcome = getOutcome(opponent,you)
    if you == you_rock:
        return outcome + 1
    elif you == you_paper:
        return outcome + 2
    elif you == you_scissor:
        return outcome + 3
    
total = 0
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        play = line.strip().split()
        # Part 1
        #total += score(play[0],play[1])
        # Part 2
        if play[1] == you_lose:
            total += score(play[0],lose(play[0]))
        elif play[1] == you_draw:
            total += score(play[0],draw(play[0]))
        elif play[1] == you_win:
            total += score(play[0],win(play[0]))

print(total)