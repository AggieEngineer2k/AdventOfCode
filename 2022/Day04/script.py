import re

def extractIds(line):
    regex = "[0-9]+"
    return [int(i) for i in re.findall(regex,str(line))]

lines = list()
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

part_1_total = 0
part_2_total = 0
for line in lines:
    ids = extractIds(line)
    left = set(range(ids[0],ids[1] + 1))
    right = set(range(ids[2],ids[3] + 1))

    if left.issubset(right) or right.issubset(left):
        part_1_total += 1

    if len(left & right) > 0:
        part_2_total += 1

print(f"Part 1: {part_1_total}")
print(f"Part 2: {part_2_total}")