total_p1 = 0
total_p2 = 0

with open('./2023/data/input_3_test.txt') as f:
    lines = f.read().splitlines()

current_number = []
start_index = None

rows = len(lines)
columns = len(lines[0])

GEAR = '*'

def is_next_to_symbol(x: int, y: int, num: list, check: str) -> bool:
    idx_y = y
    symbols = []

    for idx_x in range(x, x + len(num)):
        if idx_y > 0: symbols.append(lines[idx_y - 1][idx_x]) # UP
        if idx_y < rows - 1: symbols.append(lines[idx_y + 1][idx_x]) # DOWN
        
        if idx_x > 0: symbols.append(lines[idx_y][idx_x - 1]) # LEFT
        if idx_x < columns - 1: symbols.append(lines[idx_y][idx_x + 1]) # RIGHT

        if idx_y > 0 and idx_x > 0: symbols.append(lines[idx_y - 1][idx_x - 1]) # UP LEFT
        if idx_y > 0 and idx_x < columns - 1: symbols.append(lines[idx_y - 1][idx_x + 1]) # UP RIGHT

        if idx_y < rows - 1 and idx_x > 0: symbols.append(lines[idx_y + 1][idx_x - 1]) # DOWN LEFT
        if idx_y < rows - 1 and idx_x < columns - 1: symbols.append(lines[idx_y + 1][idx_x + 1]) # DOWN RIGHT

    if check == 'symbol':
        symbols = [symbol for symbol in symbols if not symbol.isnumeric() and symbol != '.']
    elif check == 'number':
        pass

    return len(symbols) > 0

for idx_y, line in enumerate(lines):    
    for idx_x, char in enumerate(line):
        if char.isnumeric():
            if not current_number:
                start_index = idx_x
            current_number.append(char)
        else:
            if current_number:
                next_to_symbol = is_next_to_symbol(start_index, idx_y, current_number, 'symbol')              

                if next_to_symbol:
                    total_p1 += int(''.join(current_number))
                
                current_number = []
                start_index = None

    if current_number:
        next_to_symbol = is_next_to_symbol(start_index, idx_y, current_number, 'symbol')              

        if next_to_symbol:
            total_p1 += int(''.join(current_number))
        
        current_number = []
        start_index = None 
    
print(f'Total p1: {total_p1}')
print(f'Total p1: {total_p2}')