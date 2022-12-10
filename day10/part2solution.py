lines = open("input.txt").read().split("\n")

cycle = 0
x = 1

grid = [['.' for i in range(0, 40)] for _ in range(0, 7)]


def pass_cycle(new_x):
    global x
    global cycle
    global strengths

    symbol = '#' if abs((cycle % 40) - x) <= 1 else ' '
    grid[int(cycle / 40)][cycle % 40] = symbol
    cycle = cycle + 1
    x = new_x


for line in lines:
    parts = line.split(" ")
    if parts[0] == 'noop':
        pass_cycle(x)
    else:
        pass_cycle(x)
        pass_cycle(x + int(parts[1]))

for i in grid:
    print(''.join(map(str, i)))
