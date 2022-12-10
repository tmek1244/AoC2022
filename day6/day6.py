import numpy as np
import re


def first_part():
    with open("input.txt") as f:
        input = f.readlines()

    input = input[0]

    for i in range(len(input)):
        if i < 3:
            continue

        if len(set(input[i-4:i])) == 4:
            print(i)
            print(input[i-4:i])
            return

    
def second_part():
    with open("input.txt") as f:
        input = f.readlines()

    input = input[0]
    begin = False

    for i in range(len(input)):
        if i < 13:
            continue
        
        # if not begin and len(set(input[i-4:i])) == 4:
            # print(input[i-4:i])
            # begin = True
            # i += 4
        if len(set(input[i-14:i])) == 14:
            print(i)
            print(input[i-14:i])
            return

    

def main():
    # first_part()
    second_part()
    

if __name__ == '__main__':
    main()
