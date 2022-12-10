import numpy as np
import re


def first_part():

    with open("input.txt") as f:
        input = [x.strip() for x in f.readlines()]
    
    head_position = np.array((0, 0))
    tail_position = np.array((0, 0))
    result = set()
    result.add(tuple(tail_position))

    for line in input:
        move = {
            'R': (0, 1),
            'L': (0, -1),
            'U': (1, 0),
            'D': (-1, 0)
        }[line[0]]

        for _ in range(int(line[2:])):
            head_position += move

            if abs(head_position[0] - tail_position[0]) > 1 or abs(head_position[1] - tail_position[1]) > 1:
                tail_position = head_position - move
            result.add(tuple(tail_position))
    print(len(result))
    
def print_on_screen(positions):
    print("==========================")
    board = np.zeros((5, 6))
    for i, position in enumerate(positions[::-1]):
       
        board[4 - position[0], position[1]] = len(positions) - i

    for line in board:
        for elem in line:
            if elem == 0:
                print('.', end='')
            elif elem == 1:
                print('H', end='')
            else:
                print(f'{int(elem-1)}', end='')
        print()
    print("==========================")

    
def second_part():
    with open("input.txt") as f:
        input = [x.strip() for x in f.readlines()]
    
    positions = np.array([np.array((0, 0)) for _ in range(10)])
    result = set()
    result.add(tuple(positions[-1]))

    for line in input:
        move = {
            'R': (0, 1),
            'L': (0, -1),
            'U': (1, 0),
            'D': (-1, 0)
        }[line[0]]

        for _ in range(int(line[2:])):
            positions[0] += move
            for i in range(1, len(positions)):
                if abs(positions[i-1][0] - positions[i][0]) <= 1 and abs(positions[i-1][1] - positions[i][1]) <= 1:
                    break
                if abs(positions[i-1][0] - positions[i][0]) > 0:
                    positions[i][0] += max(min(positions[i-1, 0] - positions[i, 0], 1), -1)
                if abs(positions[i-1][1] - positions[i][1]) > 0:
                    positions[i][1] += max(min(positions[i-1, 1] - positions[i, 1], 1), -1)
                
                if i == len(positions)-1:
                    result.add(tuple(positions[i]))
            # print(positions)
            # print_on_screen(positions)
    print(len(result))

def main():
    # first_part()
    second_part()
    

if __name__ == '__main__':
    main()
