def import_data(input):
    f = open(input, 'r')
    content = f.read()
    return content
crates = import_data('./input/day5.txt')
def get_crates(crates):
    s = ""
    for crate in crates.splitlines():
        s += crate + '\n'
        if crate[1] == '1':
            break
    return s.replace('[', ' ').replace(']', ' ')

def get_instructions(crates):
    s = ""
    for crate in crates.splitlines():
        if 'move' in crate:
            s += crate+'\n'
    return s

def get_items():
    lane, i, x = 1, 1, []
    while i < len(get_crates(crates).splitlines()[0]):
        for item in get_crates(crates).splitlines():
            if(str(item[i]).isupper()):
                x.append(item[i])
        i+=4
        x.append(lane)
        lane+=1
    return x

items = get_items()
def get_lanes(items):
    d, y = dict(), []
    for i in items:
        if isinstance(i, str):
            y.append(i)
        if isinstance(i, int):
            y.reverse()
            d[i] = y
            y = []
    return d

"by x, from y, to z"
def part1(items):
    d = get_lanes(items)
    inst = [int(x) for x in get_instructions(crates).split() if x.isdigit()]

    for o in range(0,len(inst),3):
        x = inst[o]
        y = inst[o+1]
        z = inst[o+2]
        for _ in range(x):
            t = d[y].pop()
            d[z].append(t)
    ANS = []
    for key, _ in d.items():
        ANS.append(d[key][-1])
    res = ''.join(ANS)
    return res

#*************************** PART 2 ***************************

def part2(items):
    d = get_lanes(items)
    inst = [int(x) for x in get_instructions(crates).split() if x.isdigit()]

    for o in range(0,len(inst),3):
        x = inst[o]
        y = inst[o+1]
        z = inst[o+2]
        if x == 1:
            for _ in range(x):
                t = d[y].pop()
                d[z].append(t)
        else:
            temp = []
            for _ in range(x):
                t = d[y].pop()
                temp.insert(0,t)
            for t in temp:
                d[z].append(t)
    ANS = []
    for key, _ in d.items():
        ANS.append(d[key][-1])
    res = ''.join(ANS)
    return res

if __name__ == '__main__':
    print(f'Part 1: {part1(items)}\nPart 2: {part2(items)}')