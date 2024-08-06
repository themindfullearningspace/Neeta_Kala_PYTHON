# input1 = input("enter")
# print(type(input1))

s = "10010"
c = int(s, 2)
print("After converting to integer base 2: ", end="")
print(c)

e = float(s)
print("After converting to float: ", end="")
print(e)

s = '4'

c = ord(s)
print("After converting character to integer: ", end="")
print(c)

c = hex(56)
print("After converting 56 to hexadecimal string: ", end="")
print(c)

c = oct(56)
print("After converting 46 to octal strinig: ", end="")
print(c)

#tuple() function is used to convert to a tuple.
#set() function returns the type after converting to set.
#list() function is used to convert any data to a list type.

s = 'geeks'

c= tuple(s)
print("After converting string to tuple: ", end="")
print(c)

c=set(c)
print("After converting string to set: ", end="")
print(c)


c = list(c)
print("After converting the string into the list ", end="")
print(c)