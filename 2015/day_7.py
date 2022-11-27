# doesn't work yet.... I hate recursion

nodes = {}

with open("./data/input_7.txt", "r") as f:
    for line in f:
        line = line.strip().split(' -> ')
        nodes[line[1]] = line[0].split()


def get_value(node):

    # if the value of searched key is an int, return it, it'll then iterate back up
    if node.isnumeric():
        return int(node)

    ins = nodes[node]

    # if the len of node is one it's either a pointer or the original value
    if len(ins) == 1:
        return get_value(ins[0])
    else:
        cmd = ins[-2]

        if cmd == 'OR':
            return get_value(ins[0]) | get_value(ins[2])
        elif cmd == 'AND':
            return get_value(ins[0]) & get_value(ins[2])
        elif cmd == 'RSHIFT':
            return get_value(ins[0]) >> get_value(ins[2])
        elif cmd == 'LSHIFT':
            return get_value(ins[0]) << get_value(ins[2]) & 65535
        elif cmd == 'NOT':
            return ~get_value(ins[1]) & 65535
        else:
            print(cmd)

    # return nodes[node]

to_find = 'a'

value = get_value(to_find)

print(value)
