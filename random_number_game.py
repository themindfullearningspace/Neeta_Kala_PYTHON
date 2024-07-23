import random

def guess_the_number():
  number_to_guess = random.randint(1, 100)
  guess = None
  
  print("I'm thinking of a number between 1 and 100.")
  
  
  while guess != number_to_guess:
    guess = int(input("Take a guess: "))
    
    if guess < number_to_guess:
      print("Higher...")
      
    elif guess > number_to_guess:
      print("Lower...")
  print("Congratulations! You guessed the number.")
  
guess_the_number()