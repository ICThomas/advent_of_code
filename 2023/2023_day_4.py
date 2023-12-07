import re

total_p1 = 0

with open('./2023/data/input_4.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    reg = re.compile('Card (.*): (.*) \| (.*)')
    card, nums, winning_nums = reg.findall(line)[0]    

    nums = [int(a) for a in nums.split(' ') if a != '']
    winning_nums = [int(a) for a in winning_nums.split(' ') if a != '']

    intersection = list(set(nums) & set(winning_nums))
    
    if intersection:
        score = (1*2**(len(intersection) - 1))
        total_p1 += score

print(f'Total p1: {total_p1}')

