with open("./data/input_1.txt", "r") as f:
    depths = [int(entry.strip()) for entry in f.readlines()]

previous = None
increased = 0

for depth in depths:
    if previous and depth > previous:
        increased += 1

    previous = depth

print(f'Total increase: {increased}')

depths_window = [depths[x-2] + depths[x-1] + depths[x] for x in range(2, len(depths))]
# print(depths_window, len(depths_window))

previous = None
increased = 0

for depth in depths_window:
    if previous and depth > previous:
        increased += 1

    previous = depth

print(f'Total increase: {increased}')
