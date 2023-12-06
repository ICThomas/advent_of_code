from functools import cmp_to_key
def read_file():
    with open("./data/input_13.txt", "r") as f:
        for pairs in f.read().split('\n\n'):
            yield list(map(eval, pairs.splitlines()))


def read_file_2():
    with open("./data/input_13.txt", "r") as f:
        return [eval(x) for x in f.read().splitlines() if x != '']


def compare_list(left, right):
    if len(left) and len(right):
        cmp = compare(left[0], right[0])
        return cmp if cmp != 0 else compare(left[1:], right[1:])
    return compare(len(left), len(right))


def compare(left, right):
    left_type = type(left)
    right_type = type(right)

    if left_type == int and right_type == int:
        return (left > right) - (left < right)
    else:
        left = left if left_type == list else [left]
        right = right if right_type == list else [right]
        return compare_list(left, right)


print(f"Part 1: {sum(index for index, x in enumerate(read_file(), 1) if compare(*x) < 0)}")

to_sort = read_file_2() + [[[2]]] + [[[6]]]

to_sort = sorted(to_sort, key=cmp_to_key(compare))

idx_1 = to_sort.index([[2]]) + 1
idx_2 = to_sort.index([[6]]) + 1

print(f"{idx_1}, {idx_2}, {idx_1 * idx_2}")
