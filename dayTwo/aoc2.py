with open("input.txt") as f:
    lines = f.readlines()

forward = 0
depth = 0
for line in lines:
      if line.split(None, 1)[0] == 'forward':
            for word in line.split():
                  if word.isdigit():
                        forward += int(word)

      elif line.split(None,1)[0] == 'up':
            for word in line.split():
                  if word.isdigit():
                        depth -= int(word)

      elif line.split(None,1)[0] == 'down':
            for word in line.split():
                  if word.isdigit():
                        depth += int(word)


print(forward)
print(depth)
print(depth * forward)
