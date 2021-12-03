import collections


with open("input.txt") as f:
    lines = f.read()

diagnostic = [s for s in lines.split() if s.isdigit()]



print(diagnostic)
index= []
newBinary =[]
for num in diagnostic:
      for i in range(len(num)):
            index.append(num[2])

print(index)
ones = index.count('0')
zeros = index.count('1')

if ones > zeros:
      print('1')
else:
      print('0')

# counter=collections.Counter(int(index))
# print(counter.keys)



# with open("input.txt") as f:
#     lines = f.read()



# diagnostic = [s for s in lines.split() if s.isdigit()]
# print(diagnostic)

# newBinary=''
# for num in diagnostic:
#       for i in num:
#             if num[i] == '1':
#                   ne


# diagnostic = [s for s in lines.split() if s.isdigit()]

# print(len(diagnostic))

# for bi in diagnostic:
#       for i in range(bi):
#             if bi[i]

# def calcualte_diagnostic(lines):
      # index = 0
      # newBinary = ''


      #       if binary[index] == '1':
      #             newBinary += '1'

      #       if binary[index] == '0':
      #             newBinary += '0'

      # split = []
      # n = 12
      # for i in range(0, len(newBinary), n):
      #       split.append(newBinary[i: i + n])
      # print (split)


# calcualte_diagnostic(lines)
