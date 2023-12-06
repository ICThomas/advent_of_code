from collections import defaultdict

elves = defaultdict(int)
current_elf = 1

with open("./data/input_1.txt", "r") as f:
    for line in f:
        line = line.strip()

        if line == '':
            current_elf += 1
            continue

        elves[current_elf] += int(line)

print(f'Total elves: {len(elves)}. Max: {max(elves.values())}')

top_3 = sum(sorted(elves.values())[-3:])

print(f'Total last 3: {top_3}')
