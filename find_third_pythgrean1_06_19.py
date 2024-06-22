#Program to find the third Pythagorean:


#import the math module to use the sqrt function
import math

def find_third_pythagorean(a, b):#defining the function that will going to find the third pythagorean 
  
  #Assuming that 'a' is the hypotenous
  if a > b:
    c_squared = a**2 - b**2
    if c_squared > 0:
      c = math.sqrt(c_squared)
      if c.is_integer():
        return int(c)
  
  #Assuming that 'b' is the hypotenous
  if b > a:
    c_squared = b**2 - a**2
    if c_squared > 0:
      c = math.sqrt(c_squared)
      if c.is_integer():
        return int(c)
      

  c_squared = a**2 + b**2
  if c_squared > 0:
    c = math.sqrt(c_squared)
    if c.is_integer():
      return int(c)
      
  #If no valid PYthagorean triplet found, return None
  return None

#Input numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

#Find the third number if it exists
result = find_third_pythagorean(a, b)

if result:
  print(f"The third number to form a Pythagorean triplet with {a} and {b} is {result}.")
else:
  print(f"There is no Pythagorean triplet that includes both {a} and {b}.")