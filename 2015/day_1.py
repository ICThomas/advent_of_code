# file contains only 1 line
with open("./2015/data/input_1.txt", "r") as f:
    instructions = f.readline()

# part 1
final_floor = sum([(1 if x == '(' else -1) for x in instructions])
print(f'Final floor: {final_floor}')

# part 2
current_floor = 0
target_floor = -1

for idx, x in enumerate(instructions):
    current_floor += 1 if x == '(' else -1
    # print(f'Current floor: {current_floor}')

    if current_floor == target_floor:
        print(f'Entered target floor at instruction: {idx+1}')
