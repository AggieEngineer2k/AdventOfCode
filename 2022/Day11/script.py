import math

class Monkey:
    items : list
    true_index : int
    false_index : int
    inspections : int = 0
    test_divisor : int
    def __init__(self, items, operation, test_divisor, true_index : int, false_index : int) -> None:
        self.items = list(items)
        self.operation = operation
        self.test_divisor = test_divisor
        self.true_index = true_index
        self.false_index = false_index
    def inspect(self):
        global monkeys, product_of_test_divisors
        self.inspections += 1
        item = self.items.pop(0)
        item = self.operation(item)
        #item = item // 3
        item = item % product_of_test_divisors
        test = (item % self.test_divisor == 0)
        if test:
            monkeys[self.true_index].items.append(item)
        else:
            monkeys[self.false_index].items.append(item)

monkeys = [
    # *** TEST ***
    # Monkey(
    #     items=[79, 98],
    #     operation=lambda x : x * 19,
    #     test=lambda x : x % 23 == 0,
    #     true_index=2,
    #     false_index=3),
    # Monkey(
    #     items=[54, 65, 75, 74],
    #     operation=lambda x : x + 6,
    #     test=lambda x : x % 19 == 0,
    #     true_index=2,
    #     false_index=0),
    # Monkey(
    #     items=[79, 60, 97],
    #     operation=lambda x : x * x,
    #     test=lambda x : x % 13 == 0,
    #     true_index=1,
    #     false_index=3),
    # Monkey(
    #     items=[74],
    #     operation=lambda x : x + 3,
    #     test=lambda x : x % 17 == 0,
    #     true_index=0,
    #     false_index=1),
    # *** INPUT ***
    Monkey(
        items=[64],
        operation=lambda x : x * 7,
        test_divisor=13,
        true_index=1,
        false_index=3),
    Monkey(items=[60, 84, 84, 65],
        operation=lambda x : x + 7,
        test_divisor=19,
        true_index=2,
        false_index=7),
    Monkey(items=[52, 67, 74, 88, 51, 61],
        operation=lambda x : x * 3,
        test_divisor=5,
        true_index=5,
        false_index=7),
    Monkey(items=[67, 72],
        operation=lambda x : x + 3,
        test_divisor=2,
        true_index=1,
        false_index=2),
    Monkey(items=[80, 79, 58, 77, 68, 74, 98, 64],
        operation=lambda x : x * x,
        test_divisor=17,
        true_index=6,
        false_index=0),
    Monkey(items=[62, 53, 61, 89, 86],
        operation=lambda x : x + 8,
        test_divisor=11,
        true_index=4,
        false_index=6),
    Monkey(items=[86, 89, 82],
        operation=lambda x : x + 2,
        test_divisor=7,
        true_index=3,
        false_index=0),
    Monkey(items=[92, 81, 70, 96, 69, 84, 83],
        operation=lambda x : x + 4,
        test_divisor=3,
        true_index=4,
        false_index=5)
]

test_divisors = [monkey.test_divisor for monkey in monkeys]
print(test_divisors)
product_of_test_divisors = math.prod(test_divisors)

for round in range(10000):
    for monkeyIndex in range(len(monkeys)):
        monkey = monkeys[monkeyIndex]
        while len(monkey.items) > 0:
            monkey.inspect()

inspections = [monkey.inspections for monkey in monkeys]
inspections.sort()
print(inspections[-1] * inspections[-2])