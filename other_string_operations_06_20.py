#String Concatenation

#e.g.1
s1 = "Hello"
s2 = "World"

print(s1 + " " +s2)

#e.g.2
s1 = "Good"
s2 = "Morning"

print(s1+" "+s2)


#Some pre-defined String Methods
s = "hello"
print(s.upper())#converting string into upper case

s = "Hello, World!"
print(s.find("World"))#return the address of the first letter

print(s.replace("World", "Python")) #Gonna replace the first agrument with the second one


#String formatting
name = "Alice"
age = 35
print(f"{name} is {age} years old.")

first_name = "John"
second_name = "Doe"
print("Hello, {} {}!".format(first_name, second_name))


#String Validations
s = "12345"
print(s.isdigit()) #Checking all the elements are numbers? #True

s= "Hello12345"
print(s.isdigit())#False

#String splitting and joining
s = "apple,banana,cherry"
print(s.split(','))#Convert the string into the list according to the arguments, you gave to it

lst = ["apple", "banana", "cherry"]
print(" ".join(lst))


#String Reversal
s="Python"
print(s[::-1])

#Palindrome check
def is_palindrome(s):
  s = s.replace(" ", "").lower()
  return s == s[::-1]

print(is_palindrome("A man a plan a canal Panama")) #True
print(is_palindrome("Hello")) #False
