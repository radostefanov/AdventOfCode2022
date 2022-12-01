import functools

file = open('input.txt')
lines = file.readlines()

res = functools.reduce(
    lambda acc, el: [0, acc[0] if acc[0] > acc[1] else acc[1]] if el == '\n' else [acc[0] + int(el), acc[1]], lines,
    [0, 0])

print(res)
