from functools import cmp_to_key

pairs = open("input.txt").read().replace("\n\n", "\n").split("\n")


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


pairs = [eval(pair) for pair in pairs]
pairs.append([[2]])
pairs.append([[6]])
new_list = sorted(pairs, key=cmp_to_key(compare_left_right), reverse=True)

mult = 1
for i, item in enumerate(new_list):
    if item == [[2]] or item == [[6]]:
        mult = mult * (i + 1)

print(mult)
