def is_nice_vowels(w: str) -> bool:
    return sum(map(w.count, "aeiou")) >= 3


def is_nice_duplicate_letter(w: str, gap: int) -> bool:
    # if gap is 0 then take next etc
    return True if [w[i] for i in range(len(w)-1-gap) if w[i] == w[i+gap+1]] else False


def is_nice_exclusions(w: str) -> bool:
    return sum(map(w.count, ['ab', 'cd', 'pq', 'xy'])) == 0


def is_nice_2_duplicates(w: str) -> bool:
    for i in range(len(w)-1):
        to_check = w[i:i+2]
        if to_check in w[i+2:]:  # to ensure no overlap
            return True
    return False


with open('./data/input_5.txt', 'r') as f:
    words = [entry.strip() for entry in f.readlines()]

nice_count_part_1 = 0
nice_count_part_2 = 0

for word in words:
    # Part 1
    vowel_check = is_nice_vowels(word)
    duplicate_check = is_nice_duplicate_letter(word, 0)
    exclusion_check = is_nice_exclusions(word)

    # Part 2
    overlap = is_nice_2_duplicates(word)
    duplicate_check_2 = is_nice_duplicate_letter(word, 1)

    if vowel_check and duplicate_check and exclusion_check:
        nice_count_part_1 += 1

    if overlap and duplicate_check_2:
        nice_count_part_2 += 1

print(f'Nice words 1: {nice_count_part_1}. Nice words 2: {nice_count_part_2}')
