file = open("input.txt").read()

for i in range(14, len(file)):
    if len(set(file[(i-14):i])) == len(file[(i-14):i]):
        print(i)
        break