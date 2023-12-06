from itertools import islice
import re

re_monkey_id = re.compile(r"Monkey\s(\d+)")
re_monkey_test = re.compile(r"Test:\sdivisible\sby\s(\d+)")
re_monkey_condition = re.compile(r"throw\sto\smonkey\s(\d+)")


class Monkey:
    def __init__(self, starting_state: list):
        self.monkey_id = re.findall(re_monkey_id, starting_state[0])[0]
        self.monkey_items = [int(x) for x in starting_state[1].split(':')[1].strip().split(',')]
        self.monkey_operation: str = starting_state[2].split(':')[1].split('=')[1].strip()
        self.monkey_test = int(re.findall(re_monkey_test, starting_state[3])[0])
        self.monkey_true_condition = int(re.findall(re_monkey_condition, starting_state[4])[0])
        self.monkey_false_condition = int(re.findall(re_monkey_condition, starting_state[5])[0])
        self.inspection_count = 0

    def evaluate_expression(self, value):
        return eval(self.monkey_operation.replace('old', str(value)))


monkey_lst = dict()

with open("./data/input_11.txt", "r") as f:
    while True:
        next_n_lines = [x.strip() for x in list(islice(f, 7))]

        if not next_n_lines:
            break

        monkey = Monkey(next_n_lines)
        monkey_lst[int(monkey.monkey_id)] = monkey

print(f'Created {len(monkey_lst)}')

ROUNDS = 20
MODULOS = 1

for _, monkey in monkey_lst.items():
    MODULOS *= monkey.monkey_test

print(
    f'Monkey Modulos: {MODULOS}'
)

for i in range(0, ROUNDS):
    for monkey_id, monkey in monkey_lst.items():
        for item in monkey.monkey_items:
            monkey.inspection_count += 1
            worry_level = monkey.evaluate_expression(item)

            if ROUNDS == 20:
                worry_level = int(worry_level // 3)
            else:
                worry_level = worry_level % MODULOS

            if worry_level % monkey.monkey_test == 0:
                monkey_target = monkey.monkey_true_condition
            else:
                monkey_target = monkey.monkey_false_condition

            monkey_lst.__getitem__(monkey_target).monkey_items.append(worry_level)

        monkey.monkey_items = []

for monkey_id, monkey in monkey_lst.items():
    print(
        f'Monkey {monkey_id}: {monkey.monkey_items}, {monkey.inspection_count}'
    )

inspections = sorted([monkey.inspection_count for _, monkey in monkey_lst.items()], reverse=True)
print(
    f'{inspections[0] * inspections[1]}'
)




