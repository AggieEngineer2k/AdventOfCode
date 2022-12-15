from anytree import Node, RenderTree, PreOrderIter

root = Node('root', type='dir')

def processLine(line : str, node : Node) -> Node:
    if line[0] == '$':
        return processCommand(line, node)
    elif line.startswith('dir'):
        name = line.split()[1]
        Node(name, parent=node, type='dir')
        return node
    elif line[0].isdigit():
        tokens = line.split()
        Node(tokens[1], parent=node, type='file', size=int(tokens[0]))
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

def getDirectorySize(node : Node) -> int:
    size = 0
    for file in [node for node in PreOrderIter(node, filter_=lambda n: hasattr(n, 'type') and n.type == 'file')]:
        size += file.size
    return size

lines = list()
with open('input.txt','r') as f:
    lines = [line.rstrip() for line in f]

currentNode = root
for line in lines:
    currentNode = processLine(line, currentNode)

totalSize = 0
for node in [node for node in PreOrderIter(root, filter_=lambda n: hasattr(n, 'type') and n.type == 'dir')]:
    size = getDirectorySize(node)
    if size <= 100000:
        totalSize += size

print(totalSize)