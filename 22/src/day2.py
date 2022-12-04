""" IT AAINT PRETTY BUT IT WORKS
    WINNER is highest score - sum of your scores each round.
    1 for X     0 for loss
    2 for Y     3 for draw
    3 for Z     6 for win

    A = rock = X
    B = paper = Y
    C = Scissors = Z
"""

''' if {choice} and {outcome}'''

guide = """
A Y
B X
C Z
"""
def import_data(input):
    f = open(input, 'r')
    content = f.read()
    
    return [game.replace(" ", "") for game in content.splitlines() if game]


def part1():
    score = 0
    games = import_data('./input/day2.txt')
    for line in games:
        if line[1] == 'X': # rock
            score += 1
            if line[0] == 'A':
                score += 3
            elif line[0] == 'B':
                score += 0
            else:
                score += 6
        elif line[1] == 'Y': # paper
            score += 2
            if line[0] == 'A':
                score += 6
            elif line[0] == 'B':
                score += 3
            else:
                score += 0
        elif line[1] == 'Z': # scissors
            score += 3
            if line[0] == 'A':
                score += 0
            elif line[0] == 'B':
                score += 6
            else:
                score += 3
    return score


def part2():
    score = 0
    games = import_data('./input/day2.txt')
    # games = [game.replace(" ", "") for game in guide.splitlines() if game]
    for play in games:
        if play[1] == 'X':
            score += 0
            if play[0] == 'A': # rock, i picked scissors
                score += 3
            elif play[0] == 'B': # paper, i picked rock
                score += 1
            else:
                score += 2
        if play[1] == 'Y':
            score += 3
            if play[0] == 'A': # rock, i picked rock
                score += 1
            elif play[0] == 'B': # paper, i picked paper
                score += 2
            else:
                score += 3
        if play[1] == 'Z':
            score += 6
            if play[0] == 'A': # rock, i picked paper
                score += 2
            elif play[0] == 'B': # paper, i picked scissors
                score += 3
            else:
                score += 1
    return score

if __name__ == '__main__':
    print(f'Part 1: {part1()}\nPart 2: {part2()}')
