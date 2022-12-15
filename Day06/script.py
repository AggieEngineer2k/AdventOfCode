line = ""
with open('input.txt') as f:
    line = f.readline()

def isMarker(substring):
    return len(substring) == len(set(substring))

for i in range(0,len(line)-4):
    if isMarker(line[slice(i,i+4)]):
        break

print(i+4)