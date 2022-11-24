# read dimensions
with open("./data/input_2.txt", "r") as f:
    lines = f.readlines()
    dimensions = [sorted(map(int, entry.strip().split('x'))) for entry in lines]


def calculate_paper(d: list) -> int:
    return (2 * d[0] * d[1]) + (2 * d[0] * d[2]) + (2 * d[1] * d[2]) + (d[0] * d[1])


def calculate_ribbon(d: list) -> int:
    return (2 * d[0]) + (2 * d[1]) + (d[0] * d[1] * d[2])


area = 0
ribbon = 0

# part 1 + 2
for dimension in dimensions:
    area += calculate_paper(dimension)
    ribbon += calculate_ribbon(dimension)

print(f'Total paper: {area}.  Total ribbon: {ribbon}')
