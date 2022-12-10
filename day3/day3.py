import numpy as np


def first_part():
    with open("input.txt") as f:
        input = f.readlines()
    
    sum = 0
    for line in input:
        for letter in line[:len(line)//2]:
            if letter in line[len(line)//2:]:
                if 'a' <= letter <= 'z':
                    sum += ord(letter) - ord('a') + 1
                else:
                    sum += ord(letter) - ord('A') + 27
                break
        
    print(sum)

    
def second_part():
    with open("input.txt") as f:
        input = f.readlines()
    
    rucksacks = np.array(input).reshape((-1, 3))
    sum = 0
    for r1, r2, r3 in rucksacks:
        for letter_1 in r1:
            if letter_1 in r2 and letter_1 in r3:
                if 'a' <= letter_1 <= 'z':
                    sum += ord(letter_1) - ord('a') + 1
                else:
                    sum += ord(letter_1) - ord('A') + 27
                break
    print(sum)


def main():
    # first_part()
    second_part()
    

if __name__ == '__main__':
    main()
