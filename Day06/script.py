line = ""
with open('input.txt') as f:
    line = f.readline()

def isMarker(substring):
    return len(substring) == len(set(substring))

# Part 1
#marking = 4
# Part 2
marking = 14

for i in range(0,len(line)-marking):
    if isMarker(line[slice(i,i+marking)]):
        break

print(i+marking)