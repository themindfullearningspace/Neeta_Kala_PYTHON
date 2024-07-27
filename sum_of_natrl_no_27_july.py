#Sum of N natural numbers in 4 ways

n = int(input("Enter a natural number: "))
i = 0
k = 0
sum1 = 0
result = 0

while i <= n: #Using 'while' loop
  sum1 += i
  i += 1
  
for k in range(1, n+1): #Using 'for' loop
  result += k
  k += 1
  
answer = n * (n+1)//2 #Using the formula

sum_range = sum(range(1, n+1)) #Using pre-defined 'sum' function along with 'range' function

  
print(f"The sum of first {n} natural number is {sum1}")
print(f"The sum of first {n} natural number is {answer}")
print(f"The sum of first {n} natural number is {result}")
print(f"The sum of first {n} natural number is {sum_range}")