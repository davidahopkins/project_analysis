import math
import re
'''you will need a space between the inches measurement
and the fraction measurement (ie 10'8" 1/2, or 10'8 1/2")'''
measurement = input("what is the meausrement you would like to convert?")
num = re.findall(r'\d+', measurement)
num_list = list(map(int, num))
list_count = int(len(num_list))
if list_count == 4:
    base_feet_frac = num_list[0]
    base_inches_frac = num_list[1]
    numerator = num_list[2]
    denominator = num_list[-1]
    inch_dec = numerator / denominator
    inches = base_inches_frac + inch_dec
    feet_dec_frac = inches / 12
    feet_frac = round(base_feet_frac + feet_dec_frac,3) #rounds to 3 decimal places    
    print(feet_frac)
elif list_count == 2:
    base_feet = num_list[0]
    base_inches = num_list[1]
    feet_dec = base_inches / 12
    feet = base_feet + feet_dec
    print(feet)
else:
    print("not a valid entry, please enter at least a foot and and inch measurement (ie 10\'8\" or 10\'8 1/2\")")