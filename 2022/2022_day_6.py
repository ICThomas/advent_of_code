
with open("./data/input_6.txt", "r") as f:
    code = f.readline().strip()

LENGTH = 4

for i in range(0, len(code)):
    marker = [a for a in code[i:i+LENGTH]]

    if len(set(marker)) == LENGTH:
        print(f'Position for length {LENGTH} is {i+LENGTH}')
        break
