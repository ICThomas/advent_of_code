with open("./data/input_2.txt", "r") as f:
    actions = [entry.strip().split(' ') for entry in f]

logic_scores = {
    # ROCK
    'A': {
        'Y': 8,  # PAPER
        'X': 4,  # ROCK
        'Z': 3,  # SCISSORS
    },
    # PAPER
    'B': {
        'Y': 5,  # PAPER
        'X': 1,  # ROCK
        'Z': 9,  # SCISSORS
    },
    # SCISSORS
    'C': {
        'Y': 2,  # PAPER
        'X': 7,  # ROCK
        'Z': 6,  # SCISSORS
    }
}

logic_result = {
    # ROCK
    'A': {
        'X': 'Z',  # LOSE
        'Y': 'X',  # DRAW
        'Z': 'Y',  # WIN
    },
    # PAPER
    'B': {
        'X': 'X',  # LOSE
        'Y': 'Y',  # DRAW
        'Z': 'Z',  # WIN
    },
    # SCISSORS
    'C': {
        'X': 'Y',  # LOSE
        'Y': 'Z',  # DRAW
        'Z': 'X',  # WIN
    }
}


total = 0
total_2 = 0

for action in actions:
    opponent, elf = action
    total += logic_scores[opponent][elf]

    # Part 2
    new_action = logic_result[opponent][elf]
    total_2 += logic_scores[opponent][new_action]

print(f'Total score 1: {total}. Total score 2: {total_2}')
