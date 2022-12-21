import itertools


input_data = """30373
25512
65332
33549
35390
"""
with open('./input/day8.txt', 'r') as f:
    # for line in f:
    #     print(line)
    data = list(list(int(n) for n in line.strip()) for line in f)
# print(data)
width = len(data[0])
height = len(data)

visible = [ [ False for _ in data[0] ] for _ in data ]

for row_n in range(height):
    # look from the left
    tallest = -1
    for col_n in range(width):
        if data[row_n][col_n] > tallest:
            tallest = data[row_n][col_n]
            visible[row_n][col_n] = True
    # look from the right
    tallest = -1
    for col_n in reversed(range(width)):
        if data[row_n][col_n] > tallest:
            tallest = data[row_n][col_n]
            visible[row_n][col_n] = True

for col_n in range(width):
    # look from the top
    tallest = -1
    for row_n in range(height):
        if data[row_n][col_n] > tallest:
            tallest = data[row_n][col_n]
            visible[row_n][col_n] = True
    # look from the bottom
    tallest = -1
    for row_n in reversed(range(height)):
        if data[row_n][col_n] > tallest:
            tallest = data[row_n][col_n]
            visible[row_n][col_n] = True

i= 0
for rows in visible:
    for columns in rows:
        if columns == True:
            i+=1
print(i)
