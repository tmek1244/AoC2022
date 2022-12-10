import numpy as np
import re


def check_reg(clock, register):
    if clock % 40 == 20:
        return register * clock
    return 0

def print_on_screen(clock, register):
    # print(register, clock, end=' ')

    if register - 1 <= (clock - 1)%40 <= register + 1:
        print('#', end='')
    else:
        print('.', end='')
    if clock % 40 == 0:
        print()

def first_part():

    with open("input.txt") as f:
        input = [x.strip() for x in f.readlines()]

    clock_counter = 0
    register = 1
    result = 0
    
    for line in input:
        clock_counter += 1
        result += check_reg(clock_counter, register)
        if line == 'noop':
            pass
        elif 'addx' in line:
            clock_counter += 1
            result += check_reg(clock_counter, register)
            register += int(line[4:])

    print(result)
    
    
def second_part():
    with open("input.txt") as f:
        input = [x.strip() for x in f.readlines()]

    clock_counter = 0
    register = 1
    
    for line in input:
        clock_counter += 1
        print_on_screen(clock_counter, register)
        if line == 'noop':
            pass
        elif 'addx' in line:
            clock_counter += 1
            print_on_screen(clock_counter, register)
            register += int(line[4:])
    
    
def main():
    # first_part()
    second_part()
    

if __name__ == '__main__':
    main()
