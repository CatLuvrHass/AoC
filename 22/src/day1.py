def import_data(text):
    f = open(text, 'r')
    content = f.read().split('\n\n')
    
    return [[int(item) for item in line.split('\n') if item] for line in content if line]

cal_count = [sum(calories) for calories in import_data('./input/day1.txt')]

cal_count.sort()
def part1(data):
    return data[-1]

def part2(data):
    return sum(data[-3:])


if __name__ == '__main__':
    print(f'Part 1: {part1(cal_count)}\nPart 2: {part2(cal_count)}')