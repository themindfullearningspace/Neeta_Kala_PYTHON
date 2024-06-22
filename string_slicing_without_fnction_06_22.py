#Function that performs the slicing

def str_slicing(str, s, e):
  while(s < e):
    print(str[s], end='')
    s += 1
  


#Taking input string
str = input("Enter the string: ")
s = int(input("Enter the start(inclusive): "))
e = int(input("Enter the end(exclusive): "))


result = str_slicing(str, s, e)
print()
