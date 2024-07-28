import random

def choose_word():
  words = ['apple', 'banana', 'grape', 'orange', 'strawberry']
  return random.choice(words)


def play():
  word = choose_word()
  word_display = "_" * len(word)
  tries = 6
  guessed = False
  guessed_letters = []
  
  print("Let's play Hangman!")
  print("Word: " + word_display)
  print("\n")
  
  
  while not guessed and tries > 0:
    guess = input("Please guess a letter: ").lower()
    
    if len(guess) == 1 and guess.isalpha():
      
      if guess in guessed_letters:
        print("You already guessed the letter", guess)
        
      elif guess not in word:
        print(guess, "is not in the word.")
        tries -= 1
        guessed_letters.append(guess)
        
      else:
        print("Good job,", guess, "is in the word!")
        guessed_letters.append(guess)
        
        word_as_list = list(word_display)
        indices = [i for i, letter in enumerate(word) if letter == guess]
        ##This list of indices is then used to update the displayed word (word_display) with the guessed letter at the correct positions
        
        for index in indices:
          word_as_list[index] = guess
          
        word_display = "".join(word_as_list)
        
        if "_" not in word_display:
          guessed = True
              
    else:
      print("Invalid input. Please guess a single letter.")
      
    print("Word: " + word_display)
    print(f"Tries remaining: {tries}")    
    print("\n")
  
  if guessed:
    print("Congratulations, you guessed the word! You win!")
    
  else:
    print(f"Sorry, you ran out of tries. The word was '{word}'. Better luck next time!.")


play()


# Detailed Breakdown:
# enumerate(word): The enumerate function takes the string word and returns an iterator that produces pairs of an index and the corresponding letter in the word. 
# For example, if word is "apple", enumerate(word) will produce (0, 'a'), (1, 'p'), (2, 'p'), (3, 'l'), (4, 'e').

# for i, letter in enumerate(word): This part of the list comprehension iterates over each index (i) and letter (letter) in the word.

# if letter == guess: This condition checks whether the current letter matches the guessed letter (guess).

# [i for i, letter in enumerate(word) if letter == guess]: The list comprehension collects the index (i) of 
# each letter that matches the guessed letter and creates a list of these indices.