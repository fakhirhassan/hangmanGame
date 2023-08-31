import random
import hangman_art
from hangman_art import stages, logo
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_word import wordlist
choice = random.choice(wordlist)
wordLenth = len(choice)
lives = 6
#Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
#Create blanks
display = []
for _ in range(wordLenth):
    display += "_"
gameEnd = False
while gameEnd:
    guess = int(input("Guess a Letter:").lower())
#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print("you've already guessed it")
    for position in range(wordLenth):
        letter = choice[position]
        if letter == guess:
            display[position] = letter
        if guess not in choice:
            print("you have guess the wrong letter")
            lives -= 1
            if lives == 0:
                gameEnd = True
                print("you lose")
#Join all the elements in the list and turn it into a String.
    print(f"{''.join(display)}")

#TODO-2: - Import the stages from hangman_art.py and make this error go away

print(stages[lives])