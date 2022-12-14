lines = open("input.txt").read().split("\n")

line_coords = []

min_x = 9999999999
max_x = 0
min_y = 99999999999
max_y = 0
for line in lines:
    coords = line.split("->")
    line = []
    for coord in coords:
        nums = coord.split(",")
        x = int(nums[0])
        y = int(nums[1])
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
        line.append((x, y))
    line_coords.append(line)

min_y = 0
grid = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

for coords in line_coords:
    prev_step = None
    for step in coords:
        if prev_step:
            if prev_step[0] == step[0]:
                dir = 1 if prev_step[1] < step[1] else -1
                for y in range(prev_step[1], step[1] + dir, dir):
                    grid[y - min_y][prev_step[0] - min_x] = '#'
            elif prev_step[1] == step[1]:
                dir = 1 if prev_step[0] < step[0] else -1
                for x in range(prev_step[0], step[0] + dir, dir):
                    grid[prev_step[1] - min_y][x - min_x] = '#'
            else:
                print("unsupported!!")
        prev_step = step

sand_start = (500,0)

total_drops = 0
def drop_sand():
    global grid
    global total_drops
    sand_x = sand_start[0] - min_x
    for y in (range(sand_start[1], max_y - min_y + 1)):
        if grid[y][sand_x] == '.':
            continue
        elif grid[y][sand_x - 1] == '.':
            sand_x = sand_x - 1
        elif grid[y][sand_x + 1] == '.':
            sand_x = sand_x + 1
        else:
            total_drops = total_drops + 1
            grid[y - 1][sand_x] = 'o'
            return

prev_total_drops = -1
while prev_total_drops != total_drops:
    prev_total_drops = total_drops
    drop_sand()

print(total_drops)
for i in grid:
    print(''.join(map(str, i)))