#Input from the user
str = input("Enter a string: ")

vowels = "aeiousAEIOU"
modified_str = ""

for char in str:
  if char in vowels:
    modified_str += '*'
  
  elif char.isalpha():
    #returns 'True' if all the characters in the string are alphabetic and there is at least one character.
    modified_str += '!'
    
  else:
    modified_str += char
    
print("Modified string:", modified_str)