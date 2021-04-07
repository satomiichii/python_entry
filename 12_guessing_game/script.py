from art import logo
import random

def game():

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # pick a random number between 1 - 100

    target_num = random.randint(1, 101)

    # set a num of attempt based on the user input

    def check_level():
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")

        if level == 'hard':
            return 5
        else:
            return 10

    attempt = check_level()
    # create a while loop that continues while the 'game_over' is false

    game_over = False

    while not game_over:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == target_num:
            print(f"You got it! The answer was {target_num}.")
            game_over = True
            break
        elif guess > target_num:
            print('Too high.')
            attempt -= 1
        else:
            print('Too low.')
            attempt -= 1
        
        if attempt == 0:
            game_over = True
            print("You've run out of guesses, you lose.")
        else:
            print('Guess again.')

game()