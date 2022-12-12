lines = list(map(lambda x: [*x], open("input.txt").read().split("\n")))

neighbours = {}
start_coords = (0, 0)
end_coords = (0, 0)


def ord_item(el):
    return ord('a' if el == 'S' else ('z' if el == 'E' else el))


def get_items_around(x, y):
    items = []
    current = ord_item(lines[y][x])
    if x > 0 and (ord_item(lines[y][x - 1]) - current) <= 1:
        items.append((x - 1, y))
    if x < len(lines[y]) - 1 and (ord_item(lines[y][x + 1]) - current) <= 1:
        items.append((x + 1, y))
    if y > 0 and (ord_item(lines[y - 1][x]) - current) <= 1:
        items.append((x, y - 1))
    if y < len(lines) - 1 and (ord_item(lines[y + 1][x]) - current) <= 1:
        items.append((x, y + 1))
    return items


for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        neighbours[(x, y)] = get_items_around(x, y)
        if lines[y][x] == 'S':
            start_coords = (x, y)
        elif lines[y][x] == 'E':
            end_coords = (x, y)

visited = []
queue = []


def bfs(node):
    global visited
    global queue

    visited.append(node)
    queue.append((node, 0))

    while queue:
        m = queue.pop(0)
        for n in neighbours[m[0]]:
            if n == end_coords:
                print(m[1] + 1)
                return
            if n not in visited:
                visited.append(n)
                queue.append((n, m[1] + 1))


bfs(start_coords)
