# Input from the user
try:
    number = int(input("Enter a number: "))
    
    # Check if the number is odd or even
    if number % 2 == 0:
        print(f"{number} is an even number.")
        #'f-strings'(formatted string literals) provide a way to embed expressions inside string literals using curly braces{}
        #Inside the curly braces, the variable 'number' is placed.
    else:
        print(f"{number} is an odd number.")
except ValueError:
    print("Invalid input. Please enter an integer.")
