import numpy as np
import re


def first_part():
    counter = 0
    with open("input.txt") as f:
        input = f.readlines()
    
    for line in input:
        m = re.search('(\d+)-(\d+),(\d+)-(\d+)', line)
        a, b, c, d = (int(x) for x in m.groups())

        if a <= c <= d <= b or c <= a <= b <= d:
            counter += 1
    
    print(counter)

    
def second_part():
    counter = 0
    with open("input.txt") as f:
        input = f.readlines()
    
    for line in input:
        m = re.search('(\d+)-(\d+),(\d+)-(\d+)', line)
        a, b, c, d = (int(x) for x in m.groups())

        if c <= a <= d or c <= b <= d or a <= c <= b:
            counter += 1
            # print(a, b, c, d)
    
    print(counter)
    

def main():
    # first_part()
    second_part()
    

if __name__ == '__main__':
    main()
