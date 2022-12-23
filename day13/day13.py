import ast

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return 1 if a < b else 0 if a == b else -1
    
    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]
    
    for i in range(max(len(a), len(b))):
        if i == len(a):
            return 1
        if i == len(b):
            return -1
        result = compare(a[i], b[i])
        if result != 0:
            return result
    return 0 


def sort(lines):
    result = []
    start_len = len(lines)
    for i in range(start_len):
        min_elem = [9999]
        for j in range(len(lines)):
            if compare(lines[j], min_elem) == 1:
                min_elem = lines[j]
        result.append(min_elem)
        lines.remove(min_elem)
    
    return result



def first_part():
    with open("input.txt") as f:
        input = f.readlines()
    
    counter = 0
    for i in range(len(input)//3 + 1):
        line1 = ast.literal_eval(input[3*i])
        line2 = ast.literal_eval(input[3*i+1])

        if compare(line1, line2) == 1:
            counter += i + 1
        # print(ast.literal_eval(line1))
        # print(ast.literal_eval(line2))
    print(counter)
            
    
def second_part():
    with open("input.txt") as f:
        input = f.readlines()

    lines = []
    for i in range(len(input)//3 + 1):
        line1 = ast.literal_eval(input[3*i])
        line2 = ast.literal_eval(input[3*i+1])

        lines.append(line1)
        lines.append(line2)
    lines.append([[2]])
    lines.append([[6]])
    
    lines = sort(lines)

    print((lines.index([[6]]) + 1)*(lines.index([[2]]) + 1))

    
def main():
    # first_part()
    second_part()
    

if __name__ == '__main__':
    main()
