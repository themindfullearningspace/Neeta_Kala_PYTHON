import random

def hangman():
    words = {
        "python": "A popular programming language",
        "java": "Another popular programming language",
        "kotlin": "A programming language used for Android development",
        "javascript": "A programming language used in web development"
    }
    word, hint = random.choice(list(words.items()))  # Randomly select a word and its hint
    guessed_letters = set()
    attempts = 6
    word_completion = "_" * len(word)  # Display blanks for the word

    print(f"Hint: {hint}")

    while attempts > 0 and "_" in word_completion:
        print("Word: ", " ".join(word_completion))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")

    if "_" not in word_completion:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Sorry, you're out of attempts. The word was: {word}")

hangman()
