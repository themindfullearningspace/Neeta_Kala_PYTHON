def count_vowels(s):
  vowels = "aeiouAEIOU"
  count = 0
  
  for char in s:
    if char in vowels:
      count += 1
  return count

#Taking input from the user
s = input("Enter the string: ")

#Counting vowels
result = count_vowels(s)

#Printing the result
print(f"The number of vowel in the string is: {result}")