with open("./data/input_9.txt", "r") as f:
    entries = [entry.strip().split(' ') for entry in f]


class Position:
    def __init__(self, name, x=0, y=0):
        self.x = x
        self.y = y
        self.name = name

    def __repr__(self):
        return f'Name: {self.name}, Location: ({self.x}, {self.y})'

    def get_position(self):
        return self.x, self.y


def move(head_tail: Position, direction_to_move: str):
    if direction_to_move == 'R':
        head_tail.x += 1
    elif direction_to_move == 'U':
        head_tail.y += 1
    elif direction_to_move == 'L':
        head_tail.x -= 1
    elif direction_to_move == 'D':
        head_tail.y -= 1


def check_tail_position(h: Position, t: Position):
    if h.get_position() == t.get_position():
        return

    if h.y == t.y and h.x - t.x == 2:
        t.x = h.x - 1
    elif h.y == t.y and h.x - t.x == -2:
        t.x = h.x + 1
    elif h.x == t.x and h.y - t.y == 2:
        t.y = h.y - 1
    elif h.x == t.x and h.y - t.y == -2:
        t.y = h.y + 1

    elif abs(h.x - t.x) == 1 and h.y - t.y == 2:
        t.x = h.x
        t.y = h.y - 1
    elif abs(h.x - t.x) == 1 and h.y - t.y == -2:
        t.x = h.x
        t.y = h.y + 1

    elif abs(h.y - t.y) == 1 and h.x - t.x == 2:
        t.y = h.y
        t.x = h.x - 1
    elif abs(h.y - t.y) == 1 and h.x - t.x == -2:
        t.y = h.y
        t.x = h.x + 1


def check_tail_position_2(h: Position, t: Position):
    pass


locations = set()

pos_head = Position('HEAD')
pos_tail = Position('TAIL')

# locations.add(pos_tail.get_position())

# Part 1
# for entry in entries:
#     direction, distance = entry[0], int(entry[1])
#
#     print(f'Moving {direction} for {distance}')
#     for _ in range(0, distance):
#
#         move(pos_head, direction)  # move head
#         locations.add(pos_tail.get_position())
#
#         check_tail_position(pos_head, pos_tail)
#
#         locations.add(pos_tail.get_position())
#
# print(len(locations))

# Part 2

positions = dict()

for i in range(0, 10):
    pos = Position(f'{i}')
    positions[i] = pos


for entry in entries:
    direction, distance = entry[0], int(entry[1])

    print(f'Moving {direction} for {distance}')
    for _ in range(0, distance):
        move(positions[0], direction)

        for j in range(0, 9):
            check_tail_position_2(positions[j], positions[j+1])

        locations.add(positions[9].get_position())

print(len(locations))
