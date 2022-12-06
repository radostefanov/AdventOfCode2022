file = open("input.txt").read()

for i in range(4, len(file)):
    if len(set(file[(i-4):i])) == len(file[(i-4):i]):
        print(i)
        break