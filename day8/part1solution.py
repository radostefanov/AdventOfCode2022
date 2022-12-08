file = list(map(lambda x: [*x], open("input.txt").read().split("\n")))


def is_visible_around(i, j, value):
    return any(
        [all(file[i][j1] < value for j1 in range(0, j)),
         all(file[i][j1] < value for j1 in range(j + 1, len(file[0]))),
         all(file[i1][j] < value for i1 in range(0, i)),
         all(file[i1][j] < value for i1 in range(i + 1, len(file)))]
    )


visible_trees = 0
for i in range(1, len(file) - 1):
    for j in range(1, len(file[i]) - 1):
        if is_visible_around(i, j, file[i][j]):
            visible_trees = visible_trees + 1

print(visible_trees + (len(file) * 2 + len(file[1]) * 2) - 4)
