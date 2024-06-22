import math


# def prft_sqroot(c_squared):
#   c = math.sqrt(c_squared)
#   if c.is_integer():
#     return int(c)

def find_third_pythagorean(a, b):
  c_squared1 = a**2 - b**2 # when 'a' is the hypoteneous
  c_squared2 = b**2 - a**2 # when 'b' is the hypoteneous
  c_squared3 = a**2 + b**2 # when 'c' is the hypoteneous
  
  if c_squared1 > 0:
    c1 = math.sqrt(c_squared1)
    if c1.is_integer():
      return int(c1)
  
  if c_squared2 > 0:
    c2 = math.sqrt(c_squared2)
    if c2.is_integer():
      return int(c2)
    
  # if c_squared3 > 0:
  #   c3 = math.sqrt(c_squared3)
  #   if c3.is_integer():
  #     return int(c3)
  
  c3 = math.sqrt(c_squared3)
  if c3.is_integer():
    return int(c3)
    
  return None


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = find_third_pythagorean(a, b)

if result:
  print(f"The pythagorean triplet for {a} and {b} is {result}.")

else:
  print(f"There is no Pythagorean triplet that includes both {a} and {b}.")