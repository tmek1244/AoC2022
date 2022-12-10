import numpy as np
import re


def first_part():
    with open("input.txt") as f:
        input = f.readlines()

    stacks = [list(x) for x in [
        "BGSC",
        "TMWHJNVG",
        "MQS",
        "BSLTWNM",
        "JZFTVGWP",
        "CTBGQHS",
        "TJPBW",
        "GDCZFTQM",
        "NSHBPF"
    ]]
    
    for line in input:
        m = re.search('move (\d+) from (\d+) to (\d+)', line)
        if m:
            amount, start, end = (int(x) for x in m.groups())
            for i in range(amount):
                stacks[end-1].append(stacks[start-1].pop())
        
    print(''.join(stack[-1] for stack in stacks))
    
def second_part():
    with open("input.txt") as f:
        input = f.readlines()

    stacks = [list(x) for x in [
        "BGSC",
        "TMWHJNVG",
        "MQS",
        "BSLTWNM",
        "JZFTVGWP",
        "CTBGQHS",
        "TJPBW",
        "GDCZFTQM",
        "NSHBPF"
    ]]
    
    for line in input:
        m = re.search('move (\d+) from (\d+) to (\d+)', line)
        if m:
            amount, start, end = (int(x) for x in m.groups())
            stacks[end-1].extend(stacks[start-1][-amount:])
            stacks[start-1] = stacks[start-1][:-amount]
    print(stacks)
    print(''.join(stack[-1] for stack in stacks))
    

def main():
    # first_part()
    second_part()
    

if __name__ == '__main__':
    main()
