with open("./data/input_10.txt", "r") as f:
    entries = [entry.strip().split(' ') for entry in f]

current_cycle = 0
end_cycle = 0
pixel_cycle = 0
next_command = None
x = 1
signal = 0

pattern = ''

def get_next_command():
    for entry in entries:
        yield entry


x_gen = get_next_command()

while True:

    if current_cycle == end_cycle or current_cycle == 0:
        if next_command:
            if next_command[0] != 'noop':
                x += int(next_command[1])

        try:
            next_command = x_gen.__next__()
        except StopIteration as e:
            break

        if next_command[0] == 'noop':
            end_cycle = current_cycle + 1
        else:
            end_cycle = current_cycle + 2

    if current_cycle % 40 == 0:
        pixel_cycle = 0

    current_cycle += 1

    if current_cycle in [20, 60, 100, 140, 180, 220]:
        signal += (current_cycle * x)

    pixel = '#' if pixel_cycle in [x-1, x, x+1] else '.'
    pattern += pixel

    pixel_cycle += 1

    if not next_command:
        break

# print(
#     f'Signal strength: {signal}'
# )
#
# print(
#     f'{pattern}'
# )

chunks = [pattern[i:i+40] for i in range(0, len(pattern), 40)]

for chunk in chunks:
    print(chunk)