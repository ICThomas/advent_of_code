import re
from collections import defaultdict
import numpy

total_p1 = 0
total_p2 = 0

GEARS = defaultdict(list)

with open('./2023/data/input_3.txt') as f:
    lines = f.read().splitlines()

def is_next_to_symbol(x: int, y: int, num: str) -> bool:
    symbols = []

    for idx_x in range(max(0, x - 1), min(len(lines[0]) - 1, x + len(num)) + 1):
        for idx_j in range(max(0, y - 1), min(len(lines) - 1, y + 1) + 1):
            value = lines[idx_j][idx_x]
            symbols.append(value)

            if value == '*':
                GEARS[(idx_j, idx_x)].append(num)

    symbols = [symbol for symbol in symbols if not symbol.isnumeric() and symbol != '.']
    
    return len(symbols) > 0

for idx_y, line in enumerate(lines):
    reg = re.compile('\d+')

    for m in reg.finditer(line):
        if is_next_to_symbol(m.start(), idx_y, m.group()):
            total_p1 += int(m.group())
    
for k, v in GEARS.items():
    total_p2 += numpy.prod([int(a) for a in v]) if len(v) == 2 else 0

print(f'Total p1: {total_p1}')
print(f'Total p1: {total_p2}')