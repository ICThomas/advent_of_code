

def get_next_line():
    with open("./data/input_25_test.txt", "r") as f:
        for row in f:
            yield row.strip()


def get_multiplier(index: int) -> int:
    if index == 0:
        return 1
    else:
        return 5**index


def convert_to_decimal(snafu: str) -> int:
    return_value = 0

    for idx, letter in enumerate(snafu):
        new_index = len(snafu) - idx - 1
        multiplier = get_multiplier(new_index)

        if letter == '-':
            value = -1
        elif letter == '=':
            value = -2
        else:
            value = int(letter)

        return_value += multiplier * value

    return return_value


for line in get_next_line():
    fuel_required = convert_to_decimal(line)

    print(
        f'Row: {line}, Fuel: {fuel_required}'
    )