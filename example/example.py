import math
import re
'''you will need a space between the inches measurement
and the fraction measurement (ie 10'8" 1/2, or 10'8 1/2")'''
measurement = input("what is the meausrement you would like to convert?")
num = re.findall(r'\d+', measurement) #extracts the numbers from the string
num_list = list(map(int, num)) #creates a list of the numbers
'''the following four lines are separating the list
items into their respective categories'''
base_feet = num_list[0] 
base_inches = num_list[1]
numerator = num_list[2]
denominator = num_list[-1]
inch_dec = numerator / denominator #getting the decimal value of inches
inches = base_inches + inch_dec 
feet_dec = inches / 12 #getting the decimal value of the inches in feet
feet = round(base_feet + feet_dec,3) #rounds to 3 decimal places
print(feet)