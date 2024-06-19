def check_palindrome(s):
  return s == s[::-1]

#Taking input string from the user
str = input("Enter the string: ")

#storing the result from the user
result = check_palindrome(str)

if result == True:
  print(f"{str} is a palindrome")

else:
  print(f"{str} is not a palindrome")
  