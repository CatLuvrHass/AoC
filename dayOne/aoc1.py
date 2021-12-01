with open("input1.txt") as f:
      contents = f.read()
      # print(contents)
            
      depths = [int(s) for s in contents.split() if s.isdigit()]
      # print(depths)

      
      if depths[0]:
            print(depths[0],'N/A - no previous measurement') 
      counter = 0
      for i in range(0, len(depths)-1):
            
            if depths[i] > depths[i+1]:
                  print(depths[i+1],'(decreased)')

            elif depths[i] < depths[i+1]:
                  print(depths[i+1],'(increased)')
                  counter +=1
      
      print(counter)