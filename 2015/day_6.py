import re
import numpy as np
import time

# Total lights: 377891. Took 8.04 second(s) - slow dictionary
# Total lights: 377891. Took 0.02 second(s) - fast numpy array

reg = re.compile(r"(turn on|turn off|toggle)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)")

with open("./data/input_6.txt", "r") as f:
    instructions = [entry.strip() for entry in f.readlines()]

lights = {}


def get_instruction(ins: str) -> list:
    op, a, b, c, d = re.findall(reg, ins)[0]
    return [op, int(a), int(b), int(c), int(d)]


start_time = time.time()

# Part 1 - dictionary
for instruction in instructions:
    cmd, x1, y1, x2, y2 = get_instruction(instruction)
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            light_key = (x, y)

            if cmd == 'turn on':
                lights[light_key] = 1
            elif cmd == 'turn off':
                lights[light_key] = 0
            elif cmd == 'toggle':
                if light_key in lights:
                    if lights[light_key] == 0:
                        lights[light_key] = 1
                    elif lights[light_key] == 1:
                        lights[light_key] = 0
                else:
                    lights[light_key] = 1

print(f'Total lights: {sum(lights.values())}. Took {time.time() - start_time:.2f} second(s)')

# Part 1 - numpy array
grid = np.zeros((1000, 1000), dtype=bool)

start_time = time.time()

for instruction in instructions:
    cmd, x1, y1, x2, y2 = get_instruction(instruction)

    x2 += 1
    y2 += 1

    width = x2 - x1
    height = y2 - y1
    mask = np.ones((height, width), dtype=bool)

    if cmd == "turn on":
        grid[y1:y2, x1:x2] = True

    if cmd == "turn off":
        grid[y1:y2, x1:x2] = False

    if cmd == "toggle":
        grid[y1:y2, x1:x2] = grid[y1:y2, x1:x2] ^ mask

print(f'Total lights: {np.sum(grid)}. Took {time.time() - start_time:.2f} second(s)')

# Part 2 - numpy array
grid2 = np.zeros((1000, 1000), dtype=int)

for instruction in instructions:
    cmd, x1, y1, x2, y2 = get_instruction(instruction)

    x2 += 1
    y2 += 1

    width = x2 - x1
    height = y2 - y1

    if cmd == "turn on":
        grid2[y1:y2, x1:x2] += 1

    if cmd == "turn off":
        grid2[y1:y2, x1:x2] -= 1
        grid2[grid2 < 0] = 0

    if cmd == "toggle":
        grid2[y1:y2, x1:x2] += 2

print(f'Total lights: {np.sum(grid2)}. Took {time.time() - start_time:.2f} second(s)')
