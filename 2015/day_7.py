nodes = {}

with open("./data/input_7.txt", "r") as f:
    for line in f:
        line = line.strip().split(' -> ')
        nodes[line[1]] = line[0].split()

print(nodes['a'])
