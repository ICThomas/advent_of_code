nodes = {}

with open("./data/input_7.txt", "r") as f:
    for line in f:
        line = line.strip().split(' -> ')
        nodes[line[1]] = line[0].split()


def get_value(node):

    # if the value of searched key is an int, return it
    if node.isnumeric():
        return node



    return nodes[node]


to_find = 'a'

value = get_value(to_find)

print(value)
