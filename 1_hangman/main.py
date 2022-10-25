from fileinput import close
from random import random
import re, random

art = """
    ------
    |    |
    O    |
  /|||\  |
   | |   |
         |
 Welcome to Hangman
"""
print(art)

# More concise way to convert the file to an array compared to the while loop
answer_pool_file = open("answers.txt", "r")
answer_pool = answer_pool_file.readlines()
answer_pool_file.close()
answer = random.choice(answer_pool).strip()

guessed_chars = [] # "answer_guessed"

for i in answer:
    if re.search("^[A-Z]$", i):
        guessed_chars.append(False)
    else:
        guessed_chars.append(True)


max_incorrect_guesses = 5
incorrect_guesses = 0

letters_guessed = []

while incorrect_guesses < max_incorrect_guesses and False in guessed_chars:
    print(f"You have {max_incorrect_guesses - incorrect_guesses} guesses left")
    
    print("Guessed letters: ", end="")
    for i in letters_guessed:
        print(i, end=", ")
    print("")

    # Display board
    for i in range(len(answer)):
        if guessed_chars[i]:
            print(answer[i], end="")
        else:
            print("_", end="")
    print("")

    # Guess input
    guess = input(">>> ")
    guess = guess.upper()

    
    if re.search("^[A-Z]$", guess) and len(guess) == 1 and guess not in letters_guessed:
        # Insert the letter guessed by the user in alphabetical order (using insertion sort)
        i = 0
        for j in letters_guessed:
            if guess < j:
                break
            i += 1

        letters_guessed.insert(i, guess)

        # Check if letter is in puzzle
        if guess in answer:
            for k in range(len(answer)):
                if guess == answer[k]:
                    guessed_chars[k] = True # Guessed correctly
        else:
            incorrect_guesses += 1

if incorrect_guesses < max_incorrect_guesses:
    print(f"Congratulations, you won! The answer was {answer}.")
else: 
    print(f"Game over, you lost. The answer was {answer}.")