import functools
import string

file = open("input.txt").read().split("\n")

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def get_weight(letter):
    if ord(letter) <= 90:
        return ord(letter) - 38
    return ord(letter) - 96

groups = list(chunks(file, 3))

sum = 0
for group in groups:
    repeats = [i for i in group[0] if i in group[1] and i in group[2]]
    sum = sum + (get_weight(list(set(repeats))[0]))


print(sum)
