#life supp = O2 * CO2

# most common is O2 0 or 1 if euqal return 1
# least common is CO2 0 or 1 if euqal return 0


with open("input.txt") as f:
    lines = f.read()
    

# print(lines)

diagnostic = [s for s in lines.split() if s.isdigit()]

def calculate_life_sup(diagnostic):
      o2 = co2 = diagnostic
      while len(o2) != 1 and len(o2) == len(co2):
            for i in range(len(diagnostic[0])):
            
                  o2_temp = co2_temp = []
                  if check_equal([x[i] for x in o2]):
                        o2_temp = [x for x in o2 if x[i] == '1']
                  else:
                        o2_temp = [x for x in o2 if x[i] == get_most_common([x[i] for x in o2])]
            
                  if check_equal([x[i] for x in co2]):
                        co2_temp = [x for x in co2 if x[i] == '0']
                  else:
                        co2_temp = [x for x in co2 if x[i] == get_least_common([x[i] for x in co2])]
                  
                  o2, co2 = o2_temp, co2_temp

      return int(o2[0],2) * int(co2[0],2)

# Helper functions
def get_most_common(arr):
    return max(set(arr), key = arr.count)


def get_least_common(arr):
    return min(set(arr), key = arr.count)


def check_equal(arr):
    return arr.count('0') == arr.count('1')


calculate_life_sup(diagnostic)
print(f'Part2: {calculate_life_sup(diagnostic)}')