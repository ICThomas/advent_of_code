with open("./data/input_7.txt", "r") as f:
    entries = [entry.strip() for entry in f]


class Node:
    def __init__(self, name, size=0, parent=None):
        self.name = name
        self.size = size
        self.parent = parent if parent else self
        self.children = []


root = Node('/')
current_node = root

for entry in entries:
    cmd = entry.split(' ')

    if cmd[1] == 'ls':
        continue

    if entry.startswith('$'):
        if cmd[2] == '/':
            current_node = root
        elif cmd[2] == '..':
            current_node = current_node.parent
        else:
            for child in current_node.children:
                if child.name == cmd[2]:
                    current_node = child
                    break
    else:
        if cmd[0] == 'dir':
            if cmd[1] not in [x.name for x in current_node.children]:
                n = Node(cmd[1], parent=current_node)
                current_node.children.append(n)

        else:
            current_node.size += int(cmd[0])


totals = []


def traverse(node):
    for c in node.children:
        node.size += traverse(c)

    totals.append(node.size)
    return node.size


traverse(root)
to_free_up = 30000000 - (70000000 - root.size)

# Part 1
print(
    sum([x for x in totals if x <= 100000])
)

# Part 2
print(
    sorted([x for x in totals if x > to_free_up])[:1]
)



