with open("./data/input_2.txt", "r") as f:
    instructions = [entry.strip().split() for entry in f.readlines()]


class Position:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_forward(self, d: int):
        self.x += d

    def move_up(self, d: int):
        self.y += d

    def move_down(self, d: int):
        self.y -= d

    def __repr__(self):
        return f'x: {self.x}, y: {self.y}. Result: {abs(self.x * self.y)}'


class Position2:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.aim = 0

    def move_forward(self, d: int):
        self.x += d
        self.y += self.aim * d

    def move_up(self, d: int):
        self.aim -= d

    def move_down(self, d: int):
        self.aim += d

    def __repr__(self):
        return f'x: {self.x}, y: {self.y}. Result: {abs(self.x * self.y)}'


# Part 1
pos = Position()

for instruction in instructions:
    ins, distance = instruction[0], int(instruction[1])

    if ins == 'forward':
        pos.move_forward(distance)
    elif ins == 'up':
        pos.move_up(distance)
    elif ins == 'down':
        pos.move_down(distance)
    else:
        print(f'Invalid command: {ins}')

print(pos)

# Part 2
pos = Position2()

for instruction in instructions:
    ins, distance = instruction[0], int(instruction[1])

    if ins == 'forward':
        pos.move_forward(distance)
    elif ins == 'up':
        pos.move_up(distance)
    elif ins == 'down':
        pos.move_down(distance)
    else:
        print(f'Invalid command: {ins}')

print(pos)
