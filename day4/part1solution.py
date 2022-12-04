import functools

file = [
    [list(map(int, [z for z in y.split("-")])) for y in x.split(",")] for x in open("input.txt").read().split("\n")
]


def contains_check(acc, e):
    if e[0][0] <= e[1][0] and e[0][1] >= e[1][1]:
        return acc + 1
    if e[1][0] <= e[0][0] and e[1][1] >= e[0][1]:
        return acc + 1
    return acc


print(functools.reduce(contains_check, file, 0))
