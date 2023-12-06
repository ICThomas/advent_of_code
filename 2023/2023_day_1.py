total_p1 = 0
total_p2 = 0

with open('./2023/data/input_1.txt') as f:
    lines = f.read().splitlines()

digits_to_replace = {
    'one': "o1ne",
    'two': "t2wo",
    'three': "t3hree",
    'four': "f4our",
    'five': "f5ive",
    'six': "s6ix",
    'seven': "s7even",
    'eight': "e8ight",
    'nine': "n9ine"
}

for line in lines:
    digits = [char for char in line if char.isnumeric()]
    total_p1 += int(digits[0] + digits[-1])

    for k, v in digits_to_replace.items():
        line = line.replace(k, v)

    digits = [char for char in line if char.isnumeric()]
    total_p2 += int(digits[0] + digits[-1])

print(f'Total p1: {total_p1}')
print(f'Total p2: {total_p2}')