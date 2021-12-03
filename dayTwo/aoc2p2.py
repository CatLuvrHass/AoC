with open("input.txt") as f:
    lines = f.readlines()

aim = 0
depth = 0
horizontal = 0
for line in lines:      
      if line.split(None,1)[0] == 'up':
            for word in line.split():
                  if word.isdigit():
                        aim -= int(word)

      elif line.split(None,1)[0] == 'down':
            for word in line.split():
                  if word.isdigit():
                        aim += int(word)
      
      elif line.split(None, 1)[0] == 'forward':
            for word in line.split():
                  if word.isdigit():
                        horizontal += int(word)
                        depth += int(word) * aim

print(horizontal)
print(depth)
print(horizontal * depth)