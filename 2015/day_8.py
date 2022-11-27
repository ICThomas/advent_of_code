import ast

with open("./data/input_8.txt", "r") as f:
    lines = [entry.strip() for entry in f.readlines()]

code_length = 0
memory_length = 0

for line in lines:
    code_length += len(line)
    memory_length += len(ast.literal_eval(line))
    # print(line, " --- ", ast.literal_eval(line))

print(f'Code length: {code_length}, memory length: {memory_length}.  Diff: {code_length - memory_length}')