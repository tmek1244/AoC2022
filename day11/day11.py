import numpy as np
import re


MONKEYS = []
MODULO = 1


class Monkey:
    def __init__(self, starting_items, operation, test, if_true, if_false) -> None:
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.counter = 0
    
    def round(self):
        for item in self.items:
            item = self.operation(item)
            # item = item//3 # first stage
            item = item % MODULO # second stage
            self.counter += 1
            if item % self.test == 0:
                MONKEYS[self.if_true].items.append(item)
            else:
                MONKEYS[self.if_false].items.append(item)
        self.items = []


def first_part():
    # MONKEYS.append(Monkey([79, 98], lambda x: x*19, 23, 2, 3))
    # MONKEYS.append(Monkey([54, 65, 75, 74], lambda x: x+6, 19, 2, 0))
    # MONKEYS.append(Monkey([79, 60, 97], lambda x: x*x, 13, 1, 3))
    # MONKEYS.append(Monkey([74], lambda x: x+3, 17, 0, 1))

    MONKEYS.append(Monkey([54, 82, 90, 88, 86, 54], lambda x: x*7, 11, 2, 6))
    MONKEYS.append(Monkey([91, 65], lambda x: x*13, 5, 7, 4))
    MONKEYS.append(Monkey([62, 54, 57, 92, 83, 63, 63], lambda x: x + 1, 7, 1, 7))
    MONKEYS.append(Monkey([67, 72, 68], lambda x: x*x, 2, 0, 6))
    MONKEYS.append(Monkey([68, 89, 90, 86, 84, 57, 72, 84], lambda x: x + 7, 17, 3, 5))
    MONKEYS.append(Monkey([79, 83, 64, 58], lambda x: x+6, 13, 3, 0))
    MONKEYS.append(Monkey([96, 72, 89, 70, 88], lambda x: x+4, 3, 1, 2))
    MONKEYS.append(Monkey([79], lambda x: x+8, 19, 4, 5))

    for _ in range(20):
        for monkey in MONKEYS:
            monkey.round()
    
    results = sorted([x.counter for x in MONKEYS])
    print(results[-1] * results[-2])
    
    
def second_part():
    MONKEYS.append(Monkey([54, 82, 90, 88, 86, 54], lambda x: x*7, 11, 2, 6))
    MONKEYS.append(Monkey([91, 65], lambda x: x*13, 5, 7, 4))
    MONKEYS.append(Monkey([62, 54, 57, 92, 83, 63, 63], lambda x: x + 1, 7, 1, 7))
    MONKEYS.append(Monkey([67, 72, 68], lambda x: x*x, 2, 0, 6))
    MONKEYS.append(Monkey([68, 89, 90, 86, 84, 57, 72, 84], lambda x: x + 7, 17, 3, 5))
    MONKEYS.append(Monkey([79, 83, 64, 58], lambda x: x+6, 13, 3, 0))
    MONKEYS.append(Monkey([96, 72, 89, 70, 88], lambda x: x+4, 3, 1, 2))
    MONKEYS.append(Monkey([79], lambda x: x+8, 19, 4, 5))

    global MODULO
    for monkey in MONKEYS:
        MODULO *= monkey.test  

    for i in range(10000):
        for monkey in MONKEYS:
            monkey.round()
        if i % 1_000 == 0:
            print(i)
    
    results = sorted([x.counter for x in MONKEYS])
    print(results[-1] * results[-2])

   
    
def main():
    # first_part()
    second_part()
    

if __name__ == '__main__':
    main()
