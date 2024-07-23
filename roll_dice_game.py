import random

def roll_dice():
  while True:
    roll = input("Roll the dice? (yes/no): ").lower()
    if roll =="yes":
      result = random.randint(1, 6)
      print(f"You rolled a {result}")
    elif roll == "no":
      print("Goodbye!")
      break
    else:
      print("Please enter 'yes' or 'no'")
      
roll_dice()