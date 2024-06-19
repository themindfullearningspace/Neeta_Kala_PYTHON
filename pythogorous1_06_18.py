#Input three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

my_tuple = (num1, num2, num3)

#Check if the numbers form a Pythagorean Triplet
if(num1 ** 2 + num2 ** 2 == num3 ** 2 ) or \
  (num2 ** 2 + num1 ** 2 == num3 ** 2) or \
  (num3 ** 2 + num3 ** 2 == num1 ** 2):
    print(f"{num1}, {num2} and {num3} form a Pythagorean Triplet.")
  
else:
  print(f"{num1}, {num2} and {num3} do not form a Pythagorean Triplet.")