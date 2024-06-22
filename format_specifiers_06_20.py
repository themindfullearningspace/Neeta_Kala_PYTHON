#Program to concatenate the string, int or any other data type
#Maybe this is the old method, now we are dealing with the thing named f-string, which will do every for us
# And for the %f and %.2f are the format specifiers for float values and the .2f means floating-point with the 2 decimal places


#Here, we are dealing with the strings
name = "Alice"
greetings = "Hello, %s" %name # %s gonna replace the other string

print(greetings)#Output: Hello, Alice



#We can do this with the integer values also
name = "Bob"
age = 25

info = "Name: %s, Age: %d" %(name, age)#for integer we are using %d
print(info)

