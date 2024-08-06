#using dict(), complex(), str()
#dict() function is used to convert a tuple of order(key, value) in a dictionary.
#str() function is used to convert integer into a string.
#complex() function is used converts real number to complex(real, imag) number.

a = 1
b = 2

tup = (('a', 1), ('b', 2), ('c', 3))

c = complex(1, 2)
print("After converting integer to complex number : ", end="")
print(c)

c = str(a)
print("After converting an integer into string: ", end="")
print(type(c))


c= dict(tup)
print("After converting tuple into the dictionary: ", end=" ")
print(c)

#Convert ASCII value to characters
a = chr(76)
b = chr(77)

print(a)
print(b)