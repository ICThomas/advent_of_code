from copy import copy

LENGTH = 12

with open("./data/input_3.txt", "r") as f:
    entries = [entry.strip() for entry in f.readlines()]

gamma = ''
epsilon = ''

for i in range(LENGTH):
    i_pos = [entry[i] for entry in entries]  # get all chars in pos over all entries

    if i_pos.count('0') > len(entries) / 2:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

total = int(gamma, 2) * int(epsilon, 2)

print(f'Part 1 Total: {total}')

# Part 2
oxy = copy(entries)
co2 = copy(entries)

for i in range(LENGTH):
    if len(oxy) == 1:
        break

    i_pos = [entry[i] for entry in oxy]
    common = '1' if i_pos.count('1') >= len(oxy) / 2 else '0'
    oxy = [entry for entry in oxy if entry[i] == common]

oxy_remainder = int(oxy[0], 2)

for i in range(LENGTH):
    if len(co2) == 1:
        break

    i_pos = [entry[i] for entry in co2]
    common = '0' if i_pos.count('1') >= len(co2) / 2 else '1'
    co2 = [entry for entry in co2 if entry[i] == common]

co2_remainder = int(co2[0], 2)

print(f'Part 2 oxy: {oxy_remainder}, co2: {co2_remainder}, total: {oxy_remainder * co2_remainder}')
