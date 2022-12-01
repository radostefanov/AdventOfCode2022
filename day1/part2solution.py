import itertools
import heapq

file = open('input.txt')
lines = file.readlines()

# parse lines into integers
lines = map(lambda e: int(e) if not e == '\n' else e, lines)

# split list into sublists divided by blank lines
lines = [list(y) for x, y in itertools.groupby(lines, lambda el: el == '\n') if not x]

# sum the sublists
lines = list(map(lambda x: sum(x), lines))

largest3 = heapq.nlargest(3, lines)

print(sum(largest3))