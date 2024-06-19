import  math


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

sum = a**2 + b**2
c = math.sqrt(sum)

if c.is_integer():
  print(f"{c}")
  
else:
  print("Both the numbers doesn't form any pythagorean Triplet.")


