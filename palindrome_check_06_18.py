str = input("Enter the string: ")

is_palindrome = True
len_str = len(str)

for i in range(len_str // 2):
  #double slash is used to get a quoitent in integer form, single slash will give us the float value
  #range will print one less number, that has been written into the samll brackets
  #here, we are not taking +1 because the indexing will start from 0 to length - 1
  if str[i] != str[len_str - i - 1]:
    is_palindrome = False
    break
  
if is_palindrome:
  print(f"{str} is a palindrome")
  
else:
  print(f"{str} is not a palindrome")
