#Sum of N natural numbers through recursion.

n = int(input("Enter a natural number: "))

if n > 0 :
  def sum_of_natrls(n):
    if n == 1:
      return 1

    else:
      return n + sum_of_natrls(n - 1)
  
  print(f"Sum is: {sum_of_natrls(n)}")
    
else:
  print("Please enter valid number")
   