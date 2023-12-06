from collections import defaultdict

with open("./data/input_3.txt", "r") as f:
    entries = [entry.strip() for entry in f]


def find_intersection(lst1: str, lst2: str) -> list:
    return list(set(lst1) & set(lst2))


def get_letter_priority(l: str) -> int:
    return ord(l.lower()) - 96 + (26 if letter.isupper() else 0)


priority = 0

for entry in entries:
    sack_1 = entry[0:len(entry) // 2]
    sack_2 = entry[len(entry) // 2:]

    # Duplicate in sacks
    for letter in find_intersection(sack_1, sack_2):
        priority += get_letter_priority(letter)

print(f'Priority: {priority}')

groups = defaultdict(list)
elf = 1

# Part 2
for idx, entry in enumerate(entries):
    groups[elf].append(entry.strip())

    if (idx + 1) % 3 == 0:
        elf += 1

priority = 0

for _, sacks in groups.items():
    duplicates = list(set(sacks[0]) & set(sacks[1])& set(sacks[2]))

    for letter in duplicates:
        priority += get_letter_priority(letter)

print(f'Priority: {priority}')
