from img_hangman import *
from words_hangman import word_list
import random

chosen_word = random.choice(word_list)
lives = 6
end_of_game = False
guessed = []
display = []

for letter in chosen_word:
    display.append('_')

print(logo)

#this line of code is only for test purpose
print(f"Pssst, the solution is {chosen_word}.")

while not end_of_game:
    guess = input('Guess a letter: ').lower()
    if guess in guessed:
        print(f"You've already guessed {guess}")
    else:
        guessed.append(guess)
        for index in range(len(chosen_word)):
            letter = chosen_word[index]
            if letter == guess:
                display[index] = letter
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win.")
            

        if lives == 0:
            end_of_game = True
            print("You loose.")
            

        print(stages[lives])

