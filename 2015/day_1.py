# file contains only 1 line
with open("./data/input_1.txt", "r") as f:
    instructions = f.readline()

# part 1
final_floor = sum([(1 if x == '(' else -1) for x in instructions])
print(f'Final floor: {final_floor}')

# part 2
current_floor = 0
target_floor = -1
trigger_instruction = None

for idx, x in enumerate(instructions):
    current_floor += 1 if x == '(' else -1

    if current_floor == target_floor:
        trigger_instruction = idx + 1
        break

print(f'Entered target floor at instruction: {trigger_instruction if trigger_instruction else "Never" }')
