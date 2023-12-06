from collections import defaultdict

boards = {}

with open("./data/input_4.txt", "r") as f:
    entries = [entry.strip() for entry in f if entry.strip() != '']

numbers = [x for x in entries[0].split(',')]

for i in range(1, len(entries[1:]), 5):
    boards[i] = [entry.split() for entry in entries[i:i+5]]


def call_number(num: str):
    for _, board in boards.items():
        for row in board:
            idx = row.index(num)

            if idx > 0:
                



for number in numbers:
    call_number(number)


