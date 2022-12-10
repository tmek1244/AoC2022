import numpy as np
import re


class Node:
    def __init__(self, size = 0, type = 'dir', name = '', parent = None) -> None:
        self.size = size
        self.children = []
        self.type = type
        self.name = name
        self.parent = parent
    
    def add_child(self, size_or_type, name):
        for child in self.children:
            if child.name == name:
                return
        size, type = (0, size_or_type) if size_or_type == 'dir' else (int(size_or_type), 'file')
        node = Node(size, type, name, self)
        self.children.append(node)

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        print(f'Not found {name}')
    
    def __repr__(self) -> str:
        return f"{self.name} {self.type} {self.size}"
    
    def set_n_get_size(self):
        if self.type == 'file':
            return self.size
        sum = 0
        for child in self.children:
            sum += child.set_n_get_size()
        
        self.size = sum

        return sum
    
    def first_part(self):
        if self.type != 'dir':
            return 0
        sum = 0
        if self.size <= 100_000:
            sum += self.size

        for child in self.children:
            sum += child.first_part()
        # print(f"{self.name} with size {sum}")
        return sum
    
    def second_part(self, limit):
        if self.type != 'dir':
            return float('inf')

        if self.size < limit:
            return float('inf')
        min_dir_size = self.size
        for child in self.children:
            min_dir_size = min(child.second_part(limit), min_dir_size)
        # print(f"{self.name} with size {sum}")
        return min_dir_size


def first_part():
    with open("input.txt") as f:
        input = [x.strip() for x in f.readlines()]

    root = None
    current_node = None
    for line_id in range(len(input)):
        if input[line_id] == '$ cd /':
            root = root if root else Node(name='/')
            current_node = root
        elif input[line_id] == '$ ls':
            line_id += 1
            while line_id < len(input) and input[line_id][0] != '$':
                m = re.search('(\w+) ([\w\.]+)', input[line_id])
                if m:
                    current_node.add_child(m.group(1), m.group(2))
                line_id += 1
            line_id -= 1
        elif input[line_id] == '$ cd ..':
            current_node = current_node.parent
        elif input[line_id][:5] == '$ cd ':
            current_node = current_node.get_child(input[line_id][5:])
    root.set_n_get_size()
    print(root.first_part())

    
def second_part():
    with open("input.txt") as f:
        input = [x.strip() for x in f.readlines()]

    root = None
    current_node = None
    for line_id in range(len(input)):
        if input[line_id] == '$ cd /':
            root = root if root else Node(name='/')
            current_node = root
        elif input[line_id] == '$ ls':
            line_id += 1
            while line_id < len(input) and input[line_id][0] != '$':
                m = re.search('(\w+) ([\w\.]+)', input[line_id])
                if m:
                    current_node.add_child(m.group(1), m.group(2))
                line_id += 1
            line_id -= 1
        elif input[line_id] == '$ cd ..':
            current_node = current_node.parent
        elif input[line_id][:5] == '$ cd ':
            current_node = current_node.get_child(input[line_id][5:])
    print(30000000 - (70_000_000 - root.set_n_get_size()))
    print(root.second_part(30000000 - (70_000_000 - root.set_n_get_size())))
    print(root.children)

def main():
    # first_part()
    second_part()
    

if __name__ == '__main__':
    main()
