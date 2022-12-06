def import_data(input):
    f = open(input, 'r')
    content = f.read()
    return [assignment for assignment in content.splitlines() if assignment]

sections = import_data('./input/day4.txt')

def parse(s):
    arr = s.split(',')
    arr.sort()
    return arr

def find_overlap_fully(arr):
    l1 = arr[0]
    l2 = arr[1]
    lower = l1.split('-')
    upper = l2.split('-')
    lower = [int(n) for n in lower]
    upper = [int(n) for n in upper]
    if (lower[0] >= upper[0] and lower[1] <= upper[1]) or (lower[0] <= upper[0] and lower[1] >= upper[1]):
        return True
    else:
        return False

def part1(sections):
    count = 0
    for s in sections:
        if find_overlap_fully(parse(s)):
            count+=1
    return count


def find_overlap_at_all(arr):
    l1 = arr[0]
    l2 = arr[1]
    lower = l1.split('-')
    upper = l2.split('-')
    lower = [int(n) for n in lower]
    upper = [int(n) for n in upper]
    if (lower[1] >= upper[0] and upper[1] >= lower[0]):
        return True
    else:
        return False

def part2(sections):
    count = 0
    for s in sections:
        if find_overlap_at_all(parse(s)):
            count+=1
    return count

if __name__ == '__main__':
    print(f'Part 1: {part1(sections)}\nPart 2: {part2(sections)}')
