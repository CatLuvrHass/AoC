#life supp = O2 * CO2

# most common is O2 0 or 1 if euqal return 1
# least common is CO2 0 or 1 if euqal return 0


with open("input.txt") as f:
    lines = f.read()

diagnostic = [s for s in lines.split() if s.isdigit()]

def calculate_life_sup(diagnostic):
      o2 = co2 = diagnostic

      for i in range(len(diagnostic[0])):
      
            inO2 = [x[i] for x in o2]
            inCO2 = [x[i] for x in co2] 

            o2_temp = co2_temp = []

            if inO2.count('0') == inO2.count('1'):
                  o2_temp = [x for x in o2 if x[i] == '1']
            else:
                  o2_temp = [x for x in o2 if x[i] == max(set(inO2), key = inO2.count)]
      
            if inCO2.count('0') == inCO2.count('1'):
                  co2_temp = [x for x in co2 if x[i] == '0']
            else:
                  co2_temp = [x for x in co2 if x[i] == min(set(inCO2), key = inCO2.count)]
            
            o2, co2 = o2_temp, co2_temp

      return int(o2[0],2) * int(co2[0],2)

calculate_life_sup(diagnostic)
print(f'Part2: {calculate_life_sup(diagnostic)}')