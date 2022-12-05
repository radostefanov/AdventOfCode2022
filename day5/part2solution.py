file = open("input.txt").read().split("\n\n")

crane_info = file[0].split("\n")
moves_info = file[1].split("\n")
crate_placement = {}

for i in range(0, len(crane_info[-1]), 4):
    items = []
    for j in crane_info:
        if i <= len(j) and j[i + 1].strip() != '':
            if not j[i + 1].isnumeric():
                items.append(j[i + 1])
            else:
                items.reverse()
                crate_placement[j[i + 1]] = items

for step in moves_info:
    step = step.replace("move ", "")
    step = list(map(int, step.replace("from", "to").split("to")))
    crate_placement[str(step[2])].extend(crate_placement[str(step[1])][-step[0]:])
    crate_placement[str(step[1])][-step[0]:] = []

response = ''.join(map(lambda x: x[-1], crate_placement.values()))
print(response)