# read dimensions
with open("./data/input_2.txt", "r") as f:
    lines = f.readlines()
    dimensions = [list(map(int, entry.strip().split('x'))) for entry in lines]


def calculate_area(d: list) -> int:
    a = d[0] * d[1]
    b = d[1] * d[2]
    c = d[0] * d[2]
    return ((a + b + c) * 2) + min(a, b, c)


area = 0

# part 1
for dimension in dimensions:
    area += calculate_area(dimension)

print(f'Total area required: {area}')
