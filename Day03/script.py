def getPriority(item):
    if ord(item) >= ord('a') and ord(item) <= ord('z'):
        return ord(item) - 96
    elif ord(item) >= ord('A') and ord(item) <= ord('Z'):
        return ord(item) - 38

lines = list()
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

total = 0

# Part 1
for line in lines:
    length = len(line)
    midpoint = length // 2
    left = set(line[0:midpoint])
    right = set(line[midpoint:length])
    shared = list(left.intersection(right))[0]
    total += getPriority(shared)
    
print(f'Part 1: {total}')

total = 0

# Part 2
groups = len(lines) // 3
for i in range(0,groups):
    elf1 = set(lines[i * 3 + 0])
    elf2 = set(lines[i * 3 + 1])
    elf3 = set(lines[i * 3 + 2])
    badge = list(elf1.intersection(elf2).intersection(elf3))[0]
    total += getPriority(badge)

print(f'Part 2: {total}')