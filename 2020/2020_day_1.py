with open("./data/input_1.txt", "r") as f:
    entries = [int(entry.strip()) for entry in f]

TARGET = 2020

for idx, entry_1 in enumerate(entries):
    for entry_2 in entries[idx:]:
        if entry_1 + entry_2 == TARGET:
            print(
                f'Entry 1: {entry_1}. Entry 2: {entry_2}. Total: {entry_1 * entry_2}'
            )
            break

for idx, entry_1 in enumerate(entries):
    for idx_2, entry_2 in enumerate(entries[idx:]):
        for entry_3 in entries[idx_2:]:
            if entry_1 + entry_2 + entry_3 == TARGET:
                print(
                    f'Entry 1: {entry_1}. Entry 2: {entry_2}. Entry 3: {entry_3}. Total: {entry_1 * entry_2 * entry_3}'
                )
                break