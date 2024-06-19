str = input("Enter the string: ")

result1 = str[3:8]#It will take from 0 to 4th index, 8 will not be included
print(result1)

result2 = str[::3]#Every skips the given number-1 character
print(result2)#If i give 2 instead of 3, it will skip one character

#Second colon is followed by a step value.
result3 = str[::]#Prints the whole output
print(result3)

result4 = str[::-1]#-1 indicates the decrement the index by one
print(result4)
# If we haven't provide any value before the first colon, then it indicates the interpreter to take the whole string

