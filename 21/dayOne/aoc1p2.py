with open("input1.txt") as f:
      contents = f.read()
      # print(contents)
            
      depths = [int(s) for s in contents.split() if s.isdigit()]
      counter=0
      for i in range(0, len(depths)-1):
            group = sum(depths[i:i+3])
            group2 = sum(depths[i+1:i+4])
            if group > group2:
                  print(group2,'decreased')
            elif group < group2:
                  print(group2,'increased')
                  counter+=1

      print(counter)