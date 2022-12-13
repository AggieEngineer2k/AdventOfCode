elves = []
calories = 0
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        # If the line is an empty string, advance to the next elf.
        if line.strip() == "":
            elves.append(calories)
            calories = 0
        else:
            calories += int(line.strip())

print(max(elves))