with open("./data/input_2.txt", "r") as f:
    entries = [entry.strip() for entry in f]


def find_letter_count(word: str, char: str) -> int:

    return word.count(char)


valid = 0
valid_2 = 0

for entry in entries:
    policy, password = entry.split(':')
    policy_range, letter = policy.split(' ')
    min_occ, max_occ = policy_range.split('-')

    letter = letter.strip()

    letter_count = find_letter_count(password, letter)

    if int(min_occ) <= letter_count <= int(max_occ):
        valid += 1

    if password[int(min_occ):int(min_occ)+1] == letter or password[int(max_occ):int(max_occ)+1] == letter:
        valid_2 += 1

    print(
        password
        , password[int(min_occ):int(min_occ)+1]
        , password[int(max_occ):int(max_occ)+1]
        , min_occ
        , int(max_occ)

    )

print(f'Valid passwords: {valid}. Valid passwords 2: {valid_2}')
