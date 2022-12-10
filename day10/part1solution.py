lines = open("input.txt").read().split("\n")

cycle = 0
x = 1
strengths = 0


def pass_cycle(new_x):
    global x
    global cycle
    global strengths
    cycle = cycle + 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        strengths = strengths + (x * cycle)
    x = new_x


for line in lines:
    parts = line.split(" ")
    if parts[0] == 'noop':
        pass_cycle(x)
    else:
        pass_cycle(x)
        pass_cycle(x + int(parts[1]))

print(strengths)
