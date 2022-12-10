import numpy as np
import re


def first_part():

    with open("input.txt") as f:
        input = [x.strip() for x in f.readlines()]
    input = map(lambda x: [int(y) for y in x], input)
    input = np.array(list(input))

    visible = np.zeros(input.shape)
    visible[0, :] = 1
    visible[-1, :] = 1
    visible[:, 0] = 1
    visible[:, -1] = 1


    for i in range(1, visible.shape[0] - 1):
        for j in range(1, visible.shape[1] - 1):
            if max(input[i, j+1:]) < input[i, j]:
                visible[i, j] = True
            elif max(input[i, :j]) < input[i, j]:
                visible[i, j] = True
            elif max(input[i+1:, j]) < input[i, j]:
                visible[i, j] = True
            elif max(input[:i, j]) < input[i, j]:
                visible[i, j] = True
    
    print(visible.sum())
    
    
def second_part():
    with open("input.txt") as f:
        input = [x.strip() for x in f.readlines()]
    input = map(lambda x: [int(y) for y in x], input)
    input = np.array(list(input))

    max_result = 0
    for i in range(input.shape[0]):
        for j in range(input.shape[1]):
            counter = 0
            result = 1
            for x in range(j+1, input.shape[1]):
                counter += 1
                if input[i, x] >= input[i, j]:
                    break
            result *= counter
            counter = 0

            for x in range(j-1, -1, -1):
                counter += 1
                if input[i, x] >= input[i, j]:
                    break
            result *= counter
            counter = 0

            for x in range(i+1, input.shape[0]):
                counter += 1
                if input[x, j] >= input[i, j]:
                    break
            result *= counter
            counter = 0

            for x in range(i-1, -1, -1):
                counter += 1
                if input[x, j] >= input[i, j]:
                    break
            result *= counter
            counter = 0

            max_result = max(max_result, result)
    
    print(max_result)

def main():
    # first_part()
    second_part()
    

if __name__ == '__main__':
    main()
