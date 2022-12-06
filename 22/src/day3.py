from errno import ERANGE
from itertools import islice

def import_data(input):
    f = open(input, 'r')
    content = f.read()
    return [sack for sack in content.splitlines() if sack]

rucksacks = import_data('./input/day3.txt')

def split(string):
    x = len(string)
    s1 = slice(0, x//2)
    s2 = slice(x//2, x)
    return s1, s2

def find_match(a, b):
    for _, ca in enumerate(a):
        for _, cb in enumerate(b):
            if ca == cb:
                return ca

def return_prio(s):
    if s.isupper():
        return ord(s) - 38
    else:
        return ord(s) - 96
        
def part1(rucksacks):
    sum_of_prios = 0
    for sack in rucksacks:
        sum_of_prios += return_prio(find_match(sack[split(sack)[0]],sack[split(sack)[1]]))
    return sum_of_prios

# ********************** PART 2 **********************

def find_match_in_group(a, b, c):
    for _, ca in enumerate(a):
        for _, cb in enumerate(b):
            for _, cc in enumerate(c):
                if ca == cb == cc:
                    return ca

def part2(vars):
    prio_of_item_types = 0
    for a, b, c in zip(*[iter(vars)]*3):
        prio_of_item_types += return_prio(find_match_in_group(a, b, c))
    return prio_of_item_types

if __name__ == '__main__':
    print(f'Part 1: {part1(rucksacks)}\nPart 2: {part2(rucksacks)}')
