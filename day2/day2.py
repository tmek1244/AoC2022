import numpy as np

LETTER_TO_VALUE = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3
}

LETTER_TO_RESULT = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

def first_part():
    with open("input.txt") as f:
        input = f.readlines()
    
    sum = 0
    for line in input:
        opponet, you = line.strip().split()
        opponet_value, you_value = LETTER_TO_VALUE[opponet], LETTER_TO_VALUE[you]

        if (opponet_value + 3 - you_value)%3 == 2:
            sum += 6
        elif opponet_value == you_value:
            sum += 3
        sum += you_value
    
    print(sum)

    
def second_part():
    with open("input.txt") as f:
        input = f.readlines()
    
    sum = 0
    for line in input:
        opponet, result = line.strip().split()
        opponet_value, result_value = LETTER_TO_VALUE[opponet], LETTER_TO_RESULT[result]

        if result == "X":
            sum += (opponet_value - 2) % 3 + 1
        elif result == "Y":
            sum += opponet_value
        else:
            sum += (opponet_value)%3 + 1 
        sum += result_value

    print(sum)


def main():
    # first_part()
    second_part()
    

if __name__ == '__main__':
    main()
