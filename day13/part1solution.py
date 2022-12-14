pairs = list(map(lambda x: x.split("\n"), open("input.txt").read().split("\n\n")))


def compare_left_right(left, right):
    for i in range(len(left)):
        if i >= len(right):
            return -1
        elif type(left[i]) is int and type(right[i]) is int:
            if left[i] < right[i]:
                return 1
            elif left[i] > right[i]:
                return -1
        else:
            next_compare = compare_left_right([left[i]] if type(left[i]) is int else left[i],
                                              [right[i]] if type(right[i]) is int else right[i])
            if next_compare != 0:
                return next_compare
    return 1 if len(left) < len(right) else 0


result = []
for pairIndex, pair in enumerate(pairs):
    left = eval(pair[0])
    right = eval(pair[1])
    if compare_left_right(left, right) != -1:
        result.append(pairIndex + 1)

print(sum(result))
