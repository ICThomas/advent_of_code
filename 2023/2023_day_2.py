from collections import defaultdict
import numpy

maximum = {
    'red': 12,
    'green': 13,
    'blue': 14
}

total = 0
total_product = 0

with open('./2023/data/input_2.txt') as f:
    for line in f:
        line = line.strip().split(":")
        id = int(line[0].replace('Game ', ''))
        result = True

        pulls = [cube.strip() for cube in line[1].split(';')]

        maximum_color = defaultdict(int)

        for pull in pulls:
            cubes = pull.split(',')

            for cube in cubes:
                amt, colour = cube.strip().split()
                amt = int(amt)

                if colour not in maximum_color:
                    maximum_color[colour] = amt
                else:
                    if amt > maximum_color[colour]:
                        maximum_color[colour] = amt

                if int(amt) > maximum[colour]:
                    result = False

        total_product += numpy.prod([a for a in maximum_color.values()])

        if result == True:
            total += id

print(f'Total p1: {total}')
print(f'Total p2: {total_product}')