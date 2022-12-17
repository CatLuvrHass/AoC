# import modules
from collections import defaultdict

# initialise variables
terminal_output = []
filepath = []
sizes = defaultdict(int)
total = 0
max_size = 100000

# read input file
with open('./input/day7.txt', 'r') as file:
    for line in file:
        terminal_output.append(line.strip())

# parse input commands
for line in terminal_output:
    # change directories
    if(line.startswith('$ cd')):
        directory = line.split()[-1]
        # go to previous directory
        if(directory == '..'):
            filepath.pop()
        # add directory to filepath
        else:
            filepath.append(directory)
    # parse ls output for sizes
    else:
        size, _ = line.split()
        if(size.isdigit()):
            size = int(size)
            for i in range(len(filepath)):
                sizes['/'.join(filepath[:i+1])] += size

def part1(sizes):
    part1_answer = sum([sizes[i] for i in sizes if sizes[i] <= 100000])
    return part1_answer

def part2(sizes):
        
    unused = 70000000 - sizes['/']
    unused_needed = 30000000 - unused
    potential_deletes = [sizes[i] for i in sizes if sizes[i] >= unused_needed]

    part2_answer = min(potential_deletes)
    return part2_answer


if __name__ == '__main__':
    print(f'Part 1: {part1(sizes)}\nPart 2: {part2(sizes)}')