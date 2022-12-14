def getPriority(item):
    if ord(item) >= ord('a') and ord(item) <= ord('z'):
        return ord(item) - 96
    elif ord(item) >= ord('A') and ord(item) <= ord('Z'):
        return ord(item) - 38

total = 0
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        length = len(line)
        midpoint = length // 2
        left = set(line[0:midpoint])
        right = set(line[midpoint:length])
        shared = list(left.intersection(right))[0]
        total += getPriority(shared)
        
print(total)