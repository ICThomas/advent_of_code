from collections import defaultdict


class Delivery:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.locations = defaultdict(int)

    def move(self, direction: str):

        if len(self.locations) == 0:
            self.deliver()

        if direction == '^':
            self.y += 1
        elif direction == '<':
            self.x -= 1
        elif direction == '>':
            self.x += 1
        elif direction == 'v':
            self.y -= 1
        else:
            print(f'Invalid command: {cmd}')

        self.deliver()

    def deliver(self):
        self.locations[(self.x, self.y)] += 1


santa = Delivery()
robot = Delivery()

# Part 1
with open("./data/input_3.txt", "r") as f:
    for cmd in f.readline():
        santa.move(cmd)

print(f'Visited houses: {len(santa.locations)}')

santa = Delivery()
robot = Delivery()

# Part 2
move_santa = True

with open("./data/input_3.txt", "r") as f:
    for cmd in f.readline():
        if move_santa:
            santa.move(cmd)
            move_santa = False
        else:
            robot.move(cmd)
            move_santa = True

unique_houses = set(santa.locations.keys()).union(robot.locations.keys())

print(f'Santa: {len(santa.locations)}. Robot: {len(robot.locations)}. Unique: {len(unique_houses)}')
