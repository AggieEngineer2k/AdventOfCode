from collections import deque

class Monkey:
    items : list
    true_index : int
    false_index : int
    inspections : int = 0
    def __init__(self, items, operation, test, true_index : int, false_index : int) -> None:
        self.items = list(items)
        self.operation = operation
        self.test = test
        self.true_index = true_index
        self.false_index = false_index
    def inspect(self):
        global monkeys
        self.inspections += 1
        item = self.items.pop(0)
        #print(f"Inspecting {item}")
        item = self.operation(item)
        #print(f"Item is now {item}")
        item = item // 3
        #print(f"Item is now {item}")
        test = self.test(item)
        #print(f"Test is {test}")
        if test:
            #print(f"Passing {item} to monkey #{self.true_index}")
            monkeys[self.true_index].items.append(item)
        else:
            #print(f"Passing {item} to monkey #{self.false_index}")
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
        test=lambda x : x % 13 == 0,
        true_index=1,
        false_index=3),
    Monkey(items=[60, 84, 84, 65],
        operation=lambda x : x + 7,
        test=lambda x : x % 19 == 0,
        true_index=2,
        false_index=7),
    Monkey(items=[52, 67, 74, 88, 51, 61],
        operation=lambda x : x * 3,
        test=lambda x : x % 5 == 0,
        true_index=5,
        false_index=7),
    Monkey(items=[67, 72],
        operation=lambda x : x + 3,
        test=lambda x : x % 2 == 0,
        true_index=1,
        false_index=2),
    Monkey(items=[80, 79, 58, 77, 68, 74, 98, 64],
        operation=lambda x : x * x,
        test=lambda x : x % 17 == 0,
        true_index=6,
        false_index=0),
    Monkey(items=[62, 53, 61, 89, 86],
        operation=lambda x : x + 8,
        test=lambda x : x % 11 == 0,
        true_index=4,
        false_index=6),
    Monkey(items=[86, 89, 82],
        operation=lambda x : x + 2,
        test=lambda x : x % 7 == 0,
        true_index=3,
        false_index=0),
    Monkey(items=[92, 81, 70, 96, 69, 84, 83],
        operation=lambda x : x + 4,
        test=lambda x : x % 3 == 0,
        true_index=4,
        false_index=5)
]

for round in range(20):
    #print(f"Round {round}")
    for monkeyIndex in range(len(monkeys)):
        monkey = monkeys[monkeyIndex]
        #print(f"Monkey {monkeyIndex} has items {monkey.items}")
        while len(monkey.items) > 0:
            monkey.inspect()
    # for monkeyIndex in range(len(monkeys)):
    #     monkey = monkeys[monkeyIndex]
    #     print(f"Monkey {monkeyIndex}: {monkey.items}")

inspections = [monkey.inspections for monkey in monkeys]
#print(inspections)
inspections.sort()
#print(inspections)
print(inspections[-1] * inspections[-2])