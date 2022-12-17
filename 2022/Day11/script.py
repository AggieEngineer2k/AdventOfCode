lines = None
with open('input.txt','r') as inputFile:
    lines = [line.rstrip() for line in inputFile]
for line in lines:
    print(line)