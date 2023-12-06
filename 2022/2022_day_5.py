from collections import defaultdict
import re
from copy import deepcopy

reg = re.compile(r"move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)")

with open("./data/input_5.txt", "r") as f:
    entries = [entry.strip('\n') for entry in f]

STACK_COUNT = 9
START_POSITION = 1

STACKS = defaultdict(list)

for entry in entries[:8]:
    print(entry)

for entry in entries[:8]:
    stack_position = START_POSITION

    for i in range(1, STACK_COUNT+1):
        crate = entry[stack_position:stack_position + 1]

        if crate != ' ':
            STACKS[i].append(crate)

        stack_position += 4

STACKS_1 = deepcopy(STACKS)
STACKS_2 = deepcopy(STACKS)


def move_crate_1(i_quantity: int, i_from: int, i_to: int):
    for _ in range(0, i_quantity):
        element = STACKS_1[i_from].pop(0)
        STACKS_1[i_to].insert(0, element)


def move_crate_2(i_quantity: int, i_from: int, i_to: int):
    crates_move = STACKS_2[i_from][:i_quantity]
    STACKS_2[i_from] = STACKS_2[i_from][i_quantity:]
    STACKS_2[i_to] = crates_move + STACKS_2[i_to]


for entry in [entry for entry in entries if 'move' in entry]:
    quantity, from_crate, to_crate = map(int, re.findall(reg, entry)[0])
    move_crate_1(quantity, from_crate, to_crate)  # PART 1
    move_crate_2(quantity, from_crate, to_crate)  # PART 2


print(
    f'Part 1: {"".join([STACKS_1[i][0] for i in range(1, STACK_COUNT+1)])}. Part 2:'
    f' {"".join([STACKS_2[i][0] for i in range(1, STACK_COUNT+1)])} '
    )

