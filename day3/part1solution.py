import functools

file = open("input.txt").read().split("\n")

def count_duplicates(acc, x):
    first_compartment = x[0:int(len(x) / 2)]
    second_compartment = x[int(len(x) / 2):]
    return acc + list(set([i for i in first_compartment if i in second_compartment]))

def get_weight(letter):
    if ord(letter) <= 90:
        return ord(letter) - 38
    return ord(letter) - 96


duplicates = functools.reduce(count_duplicates, file, [])
print(sum(map(get_weight, duplicates)))