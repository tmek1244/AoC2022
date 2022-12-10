import numpy as np


def first_part():
    max_sum = 0
    current_sum = 0

    with open("input.txt") as f:
        input = f.readlines()
    
    for line in input:
        if line == "\n":
            current_sum = 0
        else:
            current_sum += int(line.strip())

        if current_sum > max_sum:
            max_sum = current_sum
    
    print(max_sum)

def second_part():
    sums = []
    current_sum = 0

    with open("input.txt") as f:
        input = f.readlines()
    
    for line in input:
        if line == "\n":
            sums.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(line.strip())
        
    if current_sum:
        sums.append(current_sum)

    print(np.sum(sorted(sums, reverse=True)[:3]))



def main():
    # first_part()
    second_part()
    

if __name__ == '__main__':
    main()
