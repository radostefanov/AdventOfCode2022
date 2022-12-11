input = open("input.txt").read().split("\n\n")

monkeys = []

def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

class Monkey(object):
    items = []
    operation_symbol = ''
    operation_item = ''
    div_by = 0
    if_true = 0
    if_false = 0
    inspections = 0

    def __init__(self, items, operation_symbol, operation_item, div_by, if_true, if_false) -> None:
        super().__init__()
        self.items = items
        self.operation_symbol = operation_symbol
        self.operation_item = operation_item
        self.div_by = div_by
        self.if_true = if_true
        self.if_false = if_false


for monkey in input:
    lines = monkey.replace("\t","").split("\n")
    starting_items = list(map(int, lines[1].split('Starting items:')[1].split(",")))
    operation = lines[2].split("Operation: new = ")[1].split(" ")
    operation_symbol = operation[1]
    operation_item = operation[2]
    div_by = int(lines[3].split("Test: divisible by")[1])
    if_true = int(lines[4].split("If true: throw to monkey")[1])
    if_false = int(lines[5].split("If false: throw to monkey")[1])
    monkeys.append(Monkey(starting_items, operation_symbol, operation_item, div_by, if_true, if_false))

for i in range(0, 10000):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspections = monkey.inspections + 1
            other_value = (int(monkey.operation_item) if monkey.operation_item != 'old' else item)
            new_value = item * other_value if monkey.operation_symbol == '*' else item + other_value
            new_value = new_value % 9699690
            new_monkey = monkeys[monkey.if_true] if new_value % monkey.div_by == 0 else monkeys[monkey.if_false]
            new_monkey.items.append(new_value)
        monkey.items.clear()


inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)
print(inspections[0] * inspections[1])