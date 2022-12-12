import numpy as np
import re
import queue


def first_part():
    with open("input.txt") as f:
        input = [list(x.strip()) for x in f.readlines()]
    
    input = np.array(input)
    visited = np.full(input.shape, -1)
    start = np.argwhere(input=='S')[0]
    end = np.argwhere(input=='E')[0]

    input[tuple(start)] = 'a'
    input[tuple(end)] = 'z' 
    q = queue.Queue()

    q.put((start, 0))

    while not q.empty():
        pos, dist = q.get()
        if visited[tuple(pos)] != -1:
            continue
        visited[tuple(pos)] = dist
        if tuple(pos) == tuple(end):
            break
        if pos[0] > 0 and ord(input[tuple(pos)]) + 1 >= ord(input[pos[0]-1, pos[1]]):
            q.put(((pos[0]-1, pos[1]), dist+1))
        if pos[0] < visited.shape[0] - 1 and ord(input[tuple(pos)]) + 1 >= ord(input[pos[0]+1, pos[1]]):
            q.put(((pos[0]+1, pos[1]), dist+1))
        if pos[1] > 0 and ord(input[tuple(pos)]) +1 >= ord(input[pos[0], pos[1]-1]):
            q.put(((pos[0], pos[1]-1), dist+1))
        if pos[1] < visited.shape[1] - 1 and ord(input[tuple(pos)]) +1 >= ord(input[pos[0], pos[1]+1]):
            q.put(((pos[0], pos[1]+1), dist+1))

    print(visited[tuple(end)])
    
    
def second_part():
    with open("input.txt") as f:
        input = [list(x.strip()) for x in f.readlines()]
    
    input = np.array(input)
    visited = np.full(input.shape, -1)
    start = np.argwhere(input=='E')[0]
    end = np.argwhere(input=='S')[0]

    input[tuple(end)] = 'a'
    input[tuple(start)] = 'z' 
    q = queue.Queue()

    q.put((start, 0))

    while not q.empty():
        pos, dist = q.get()
        if visited[tuple(pos)] != -1:
            continue
        visited[tuple(pos)] = dist
        if input[tuple(pos)] == 'a':
            print(dist)
            break
        if pos[0] > 0 and ord(input[tuple(pos)]) - 1 <= ord(input[pos[0]-1, pos[1]]):
            q.put(((pos[0]-1, pos[1]), dist+1))
        if pos[0] < visited.shape[0] - 1 and ord(input[tuple(pos)]) - 1 <= ord(input[pos[0]+1, pos[1]]):
            q.put(((pos[0]+1, pos[1]), dist+1))
        if pos[1] > 0 and ord(input[tuple(pos)]) - 1 <= ord(input[pos[0], pos[1]-1]):
            q.put(((pos[0], pos[1]-1), dist+1))
        if pos[1] < visited.shape[1] - 1 and ord(input[tuple(pos)]) - 1 <= ord(input[pos[0], pos[1]+1]):
            q.put(((pos[0], pos[1]+1), dist+1))

    
def main():
    # first_part()
    second_part()
    

if __name__ == '__main__':
    main()
