Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... # List of possible words for the game
... word_list = ['python', 'hangman', 'programming', 'developer', 'algorithm', 'computer', 'function']
... 
... def display(word, guessed_letters):
...     """
...     Display the word with guessed letters and underscores for unguessed letters.
...     """
...     displayed_word = ''
...     for letter in word:
...         if letter in guessed_letters:
...             displayed_word += letter
...         else:
...             displayed_word += '_'
...     return displayed_word
... 
... def hangman():
...     print("Welcome to Hangman!")
...     
...     # Randomly select a word from the word list
...     word = random.choice(word_list)
...     guessed_letters = []  # List to store guessed letters
...     incorrect_guesses = 0  # Counter for incorrect guesses
...     max_incorrect_guesses = 6  # Maximum number of incorrect guesses allowed
...     
...     while incorrect_guesses < max_incorrect_guesses:
...         print(f"\nWord: {display(word, guessed_letters)}")
...         print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
...         
...         # Get the player's guess
...         guess = input("Guess a letter: ").lower()
...         
...         # Check if the input is a valid single letter
...         if len(guess) != 1 or not guess.isalpha():
...             print("Please enter a valid single letter.")
...             continue
...         
...         # Check if the letter has already been guessed
...         if guess in guessed_letters:
...             print("You've already guessed that letter. Try again.")
...             continue
...         
...         # Add the guessed letter to the list of guessed letters
...         guessed_letters.append(guess)
        
        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.")
        
        # Check if the player has guessed the word correctly
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nGame Over! You've run out of guesses. The word was: {word}")

# Start the game
hangman()
