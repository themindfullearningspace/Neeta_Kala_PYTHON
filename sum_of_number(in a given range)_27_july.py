#Adding the natural number in a certain range.
  
start = int(input("Enter the first number of the range: "))
end = int(input("Enter the last number of the range: "))

if  start > 0 and end >= start :
  result = 0
  i = start
  
  while i <= end:
    result += i
    i += 1
    
  print(result)
  
else:
  print("Please enter valid numbers")
