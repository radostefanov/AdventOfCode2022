import math

file = list(map(lambda x: [*x], open("input.txt").read().split("\n")))


def visibility_score(i, j, value):
    visibility = [0, 0, 0, 0]
    for j1 in reversed(range(0, j)):
        visibility[0] = visibility[0] + 1
        if file[i][j1] >= value:
            break
    for j1 in range(j + 1, len(file[0])):
        visibility[1] = visibility[1] + 1
        if file[i][j1] >= value:
            break
    for i1 in reversed(range(0, i)):
        visibility[2] = visibility[2] + 1
        if file[i1][j] >= value:
            break
    for i1 in range(i + 1, len(file)):
        visibility[3] = visibility[3] + 1
        if file[i1][j] >= value:
            break
    return math.prod(visibility)


max_visibility = 0
for i in range(1, len(file) - 1):
    for j in range(1, len(file[i]) - 1):
        visibility = visibility_score(i, j, file[i][j])
        if visibility > max_visibility:
            max_visibility = visibility
print(max_visibility)
