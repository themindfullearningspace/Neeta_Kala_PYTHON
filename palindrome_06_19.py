def is_palindrome(s):
  if s == s[::-1]:
    return True
  
  else:
    return False
  
  
#Taking input from the user
str = input("Enter a string: ")

# result= is_palindrome()

if is_palindrome(str)==True:
  print(f"{str} is a palindrome")  

else:
  print(f"{str} is not a palindrome")