# Input from the user
str = input("Enter a string: ")

# Print the reversed string
print("Reversed string: ", end="")

for i in range(len(str) - 1, -1, -1):
    print(str[i], end="")
    
print()#Ensures that the output ends with a newline.


#A 'for' loop with range(len(str) -1 ,-1, -1)' starts from the last character and decrements until the first character.
#Each character is printed in reverse order using 'print(str[i], end="")' to avoid newlines after each character