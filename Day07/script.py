from anytree import search, Node, RenderTree, find

root = Node("root")

def processLine(line : str, node : Node) -> Node:
    if line[0] == '$':
        return processCommand(line, node)
    elif line.startswith('dir'):
        name = line.split()[1]
        Node(name, parent=node)
        return node
    else:
        return node

def processCommand(line : str, node : Node) -> Node:
    if line == '$ cd /':
        return root
    elif line == '$ cd ..':
        return node.parent
    elif line.startswith('$ cd '):
        name = line.split()[2]
        return [child for child in node.children if child.name == name][0]
    else:
        return node

lines = list()
with open('input.txt','r') as f:
    lines = [line.rstrip() for line in f]

node = root
for line in lines:
    print(line)
    node = processLine(line, node)

print(RenderTree(root))