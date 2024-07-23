import random

def rock_paper_scissors():
  choices = ["rock", "paper", "scissors"] #Possible choices
  computer_choice = random.choice(choices) #computer randomly selects one of the choices
  player_choice = input("Enter rock, paper, or scissors: ").lower() #Player inputs their choice
  
  if player_choice == computer_choice:
    print(f"It's a tie! Both chose {player_choice}")
    
  elif(player_choice == "rock" and computer_choice == "scissors") or \
      (player_choice == "paper" and computer_choice == "rock") or \
      (player_choice == "scissors" and computer_choice == "paper"):
      print(f"You win! {player_choice} beats {computer_choice}.")
      
  else:
    print(f"You lose! {computer_choice} beats {player_choice}.")
    
rock_paper_scissors()