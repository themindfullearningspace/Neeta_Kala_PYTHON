number = int(input("Enter the number: "))
power = len(str(number))
temp = number

ans = 0
while(temp > 0):
  r = temp % 10
  ans = (r ** power) + ans
  temp = temp // 10
  
if int(number) == ans:
  print("The number is amstrong number")
  
else:
  print("The number is not the armstrong number.")