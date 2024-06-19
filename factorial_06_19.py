def factorial(n):
  if n == 0:
    return 1
  
  else:
    return n * factorial(n-1)
  
#Taking the number as input
num = int(input("Enter the number: "))


#Calculating the factorial
result = factorial(num)

#Printing the result
print(f"The factorial of {num} is {result}")