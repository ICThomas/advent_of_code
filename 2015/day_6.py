import re

with open("./data/input_6.txt", "r") as f:
    instructions = [entry.strip() for entry in f.readlines()]

for instruction in instructions:
    reg = re.compile(r"(turn on|turn off|toggle)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)")
    values = re.findall(reg, instruction)
    print(instruction, values)
