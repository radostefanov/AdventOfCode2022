steps = list(map(lambda x: [x.split(" ")[0], int(x.split(" ")[1])], open("input.txt").read().split("\n")))

head_coords = (50, 50)
tail_coords = (50, 50)

tail_history = [tail_coords]


def update_tail(t_coords, h_coords):
    global tail_history
    t_coords = [t_coords[0], t_coords[1]]
    if abs(t_coords[0] - h_coords[0]) <= 1 and abs(t_coords[1] - h_coords[1]) <= 1:
        return t_coords[0], t_coords[1]

    if t_coords[0] == h_coords[0]:
        t_coords[1] = t_coords[1] + (1 if h_coords[1] > t_coords[1] else -1)
    elif t_coords[1] == h_coords[1]:
        t_coords[0] = t_coords[0] + (1 if h_coords[0] > t_coords[0] else -1)
    else:
        t_coords[0] = t_coords[0] + (1 if h_coords[0] > t_coords[0] else -1)
        t_coords[1] = t_coords[1] + (1 if h_coords[1] > t_coords[1] else -1)

    tail_history.append((t_coords[0], t_coords[1]))
    return t_coords[0], t_coords[1]


for step in steps:
    for _ in range(0, step[1]):
        if step[0] == 'R':
            head_coords = (head_coords[0] + 1, head_coords[1])
        elif step[0] == 'L':
            head_coords = (head_coords[0] - 1, head_coords[1])
        elif step[0] == 'U':
            head_coords = (head_coords[0], head_coords[1] - 1)
        elif step[0] == 'D':
            head_coords = (head_coords[0], head_coords[1] + 1)
        tail_coords = update_tail(tail_coords, head_coords)

print(len(set(tail_history)))
