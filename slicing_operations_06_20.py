#In this program, we are demonstrating that how can we declare the strings in different ways


#With double quotation (single pair)
str1 = "Namaste, Duniya!"
print(str1)

#with single quotations (single pair)
str2 = 'Hello, World'
print(str2)

#By using triple single quotes(''') 
str3 = '''Camel Case'''
print(str3)

#By using triple double quores
str4 = """This is a string which is using triple double quotes"""
print(str4)

#If we want to change the lines of the strings then we can do it like in this way.
str5 = """Durga
soft"""
print(str5)


#If we want to do some quotation then, we can use the combination of double and single ones.
str6 = '''This  is a "character6."'''
print(str6)


str7 = "This is another 'character7'"
print(str7)

str8 = 'This is one more "character8"'
print(str8)

str='c' #we can represent char values also by following the same thing, explicity char type is not available
print("hello",type(str))



#Slicing of Strings:
#1. slice means a piece
#2.[] operator is called slice operator, which can be used to retrive parts of String.
#3.Python Strings follows zero based index.
#4.The index can be either +ve or -ve.
#5. +ve index means forward direction from left to right.
#6. -ve index means backward direction from right to left
#-5 -4  -3  -2  -1
#0   1   2   3   4


print(str1[-1])#i.e. indexed s[4]

print(str1[-4])#i.e. indexed s[1]

#print(str1[40]) #Throws an error message that the 'index is out of the range'

print(str1[2:40]) # from index 2 to the whole string

print(str1[1:])#from index 1 to the whole string

print(str1[:4])#printing the string from the index 0 upto index 4

print(f"Printing the special string: {str1[:]}")

print(str1*3)#printing the string thrice

len(str1)

result1 = str1[3:8]#It will take from 0 to 4th index, 8 will not be included
print(result1)

result2 = str1[::3]#Every skips the given number-1 character
print(result2)#If i give 2 instead of 3, it will skip one character

#Second colon is followed by a step value.
result3 = str1[::]#Prints the whole string
print(result3)

result4 = str1[::-1]#-1 indicates the decrement the index by one
print(result4)
# If we haven't provide any value before the first colon, then it indicates the interpreter to take the whole string

