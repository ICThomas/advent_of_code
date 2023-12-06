with open("./data/input_4.txt", "r") as f:
    entries = [entry.strip() for entry in f]


def find_intersection(lst1: list, lst2: list) -> list:
    return list(set(lst1) & set(lst2))


fully_intersect = 0
assignment_count = 0
overlap = 0

for entry in entries:
    assignment_1, assignment_2 = entry.split(',')

    assignment_1_start = int(assignment_1.split('-')[0])
    assignment_1_end = int(assignment_1.split('-')[1])

    assignment_2_start = int(assignment_2.split('-')[0])
    assignment_2_end = int(assignment_2.split('-')[1])

    lst_1 = [x for x in range(assignment_1_start, assignment_1_end + 1)]
    lst_2 = [x for x in range(assignment_2_start, assignment_2_end + 1)]

    intersect = find_intersection(lst_1, lst_2)

    if len(intersect) == min(len(lst_1), len(lst_2)):
        fully_intersect += 1

    if len(intersect) > 0:
        overlap += 1

    assignment_count += 1

print(f'Total: {fully_intersect} / {assignment_count}. Overlap: {overlap}')
