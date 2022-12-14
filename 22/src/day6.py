def import_data(text):
    f = open(text, 'r')
    content = f.read()
    return content

input_data = import_data('./input/day6.txt')

def part1(max_allowed):
    for i in range(len(input_data) - max_allowed + 1):

        window = input_data[i: i + max_allowed]
        if(len(set(window)) == len(window)):
            return i + max_allowed

if __name__ == '__main__':
    print(f'Part 1: {part1(max_allowed=4)}\nPart 2: {part1(max_allowed=14)}')