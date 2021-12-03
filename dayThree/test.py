

with open("input.txt") as f:
    lines = f.read()

print(lines)

diagnostic = [s for s in lines.split() if s.isdigit()]

# print(diagnostic)
gamma =''

for i in range(len(diagnostic[0])):

      index = [x[i] for x in diagnostic]
      most_common = max(set(index), key = index.count)
      gamma+=most_common


print(gamma)
opposite = { '0':'1', '1':'0'}
rev = [''.join(opposite[c] for c in n) for n in gamma]
print(rev)
epsilon = ''.join([str(elem) for elem in rev])
print(epsilon)

result = int(gamma,2) * int(epsilon,2)
print(result)
