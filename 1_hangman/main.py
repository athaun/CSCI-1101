import re

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

answer = "What's Up, Doc?".upper()

answer_guessed = []

for i in answer:
    if re.search("^[A-Z]$", i):
        answer_guessed.append(False)
    else:
        answer_guessed.append(True)


max_incorrect_guesses = 5
incorrect_guesses = 0

letters_guessed = []

while incorrect_guesses < max_incorrect_guesses and False in answer_guessed:
    print(f"You have {max_incorrect_guesses - incorrect_guesses} guesses left")
    # for i in answer:
    #     if answer_guessed[i]
