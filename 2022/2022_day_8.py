with open("./data/input_8.txt", "r") as f:
    entries = [entry.strip() for entry in f]

height, width = len(entries), len(entries[0])
total_visible = 0


def get_column(col: int) -> str:
    column = []

    for entry in entries:
        column.append(entry[col])
    return ''.join(column)


def reverse_list(lst: list) -> list:
    return [a for a in reversed(lst)]


for y, line in enumerate(entries):
    for x, value in enumerate(line):
        value = int(value)

        # edges
        if x == 0 or y == 0 or x == width - 1 or y == height - 1:
            total_visible += 1
            continue

        # middle
        visible_left = value > max([int(a) for a in line[:x]])
        visible_right = value > max([int(a) for a in line[x+1:]])

        y_column = [int(entry[x]) for entry in entries]

        visible_up = value > max([a for a in y_column[:y]])
        visible_down = value > max(a for a in y_column[y+1:])

        if visible_left or visible_right or visible_up or visible_down:
            total_visible += 1

print(
    f'Visible: {total_visible}'
)

# for entry in entries:
#     print(entry)

max_scenic_score = 0


def get_scenic_score(lst: list, v: int) -> int:
    score = 0

    for tree_size in lst:
        score += 1

        if tree_size >= v:
            break

    return score


# Part 2
for y, line in enumerate(entries):

    for x, value in enumerate(line):
        value = int(value)

        score_left, score_right, score_up, score_down = 0, 0, 0, 0

        left = [int(a) for a in line[:x]]
        right = [int(a) for a in line[x+1:]]

        y_column = [int(entry[x]) for entry in entries]
        up = y_column[:y]
        down = y_column[y+1:]

        # LEFT
        if x > 0:
            score_left += get_scenic_score(reverse_list(left), value)

        # RIGHT
        if x < width - 1:
            score_right += get_scenic_score(right, value)

        # DOWN
        if y < height - 1:
            score_down += get_scenic_score(down, value)

        # UP
        if y > 0:
            score_up += get_scenic_score(reverse_list(up), value)

        scenic = score_left * score_right * score_up * score_down
        max_scenic_score = max(max_scenic_score, scenic)

        # print(
        #     f'X: {x}, Y: {y}, Value: {value}, Scenic: {scenic}, Left: {score_left}, Right: {score_right}, Up: {score_up}, Down: {score_down}'
        # )

print(max_scenic_score)

