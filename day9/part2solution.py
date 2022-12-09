steps = list(map(lambda x: [x.split(" ")[0], int(x.split(" ")[1])], open("input.txt").read().split("\n")))

head_coords = (50, 50)
other_coords = [(50, 50) for _ in range(0, 9)]

tail_history = [head_coords]


def update_tail(t_coords, h_coords, is_tail=False):
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

    if is_tail:
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

        for i in range(0, 9):
            prev_coord = head_coords if i == 0 else other_coords[i - 1]
            other_coords[i] = update_tail(other_coords[i], prev_coord, i == 8)

print(len(set(tail_history)))
