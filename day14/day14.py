import numpy as np


def print_out_board(board):
    for row in range(len(board)):
        for col in range(board.shape[1]):
            if board[row, col] == 0:
                print('.', end='')
            elif board[row, col] == 1:
                print('#', end='')
            elif board[row, col] == 2:
                print('o', end='')
        print()
    print()
                

def simulate(input, ground=False):
    max_overall_row = 0
    board = np.zeros((200, 500))
    for line in input:
        prev_row, prev_col = None, None
        for point in line.strip().replace(' ', '').split('->'):
            col, row  = point.split(',')
            row, col = int(row), int(col) - 250

            if prev_col and prev_row:
                min_row, max_row = min(prev_row, row), max(prev_row, row)
                min_col, max_col = min(prev_col, col), max(prev_col, col)

                board[min_row:max_row+1, min_col: max_col+1] = 1
            max_overall_row = max(max_overall_row, row)
            prev_row, prev_col = row, col

    max_overall_row += 2
    if ground:
        board[max_overall_row] = 1

    drop_out = False
    counter = 0
    while not drop_out:
        sand = 0, 250
        if board[sand[0], sand[1]] != 0:
            break

        while True:
            if sand[0] > 195:
                drop_out = True
                break
            if board[sand[0]+1, sand[1]] == 0:
                sand = sand[0] + 1, sand[1]
            elif board[sand[0] + 1, sand[1] - 1] == 0:
                sand = sand[0] + 1, sand[1] - 1
            elif board[sand[0] + 1, sand[1] + 1] == 0:
                sand = sand[0] + 1, sand[1] + 1
            else:
                board[sand[0], sand[1]] = 2
                counter += 1
                break
    print_out_board(board)
    print(counter)


def first_part():
    with open("input.txt") as f:
        input = f.readlines()
    simulate(input)
            
    
def second_part():
    with open("input.txt") as f:
        input = f.readlines()
    simulate(input, True)
    
    
def main():
    # first_part()
    second_part()
    

if __name__ == '__main__':
    main()
