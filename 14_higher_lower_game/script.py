from art import logo, vs
from game_data import data
import random
import os


def clear():
    """Clear console"""
    os.system('cls' if os.name == 'nt' else 'clear')

# Create a function to run game.


def game(person='', score=0):
    
    print(logo)

    # pick random data from the data list and store them in variables.

    data_a = random.choice(data)
    data_b = random.choice(data)

    # check if the call is recursively made = person parameter has a data.
    # If so, store the previous person in data_A and print current score.

    if person != '':
        data_a = person
        print(f"You're right! Current score: {score}.")

    while data_a == data_b:
        data_b = random.choice(data)

    # print opponents and ask user to choose from A or B.

    print(f"Compare A: {data_a['name']}, {data_a['description']}, from {data_a['country']}.")
    print(vs)
    print(f"Against B: {data_b['name']}, {data_b['description']}, from {data_b['country']}.")

    guess = input("Who has more followers? Type 'A' or 'B': ")

    # create check_answer function to check the users answer. 

    def check_answer(user_guess):
        """a function that takes a user's guess and returns boolean for as a game result"""
        if user_guess == 'A':
            return data_a['follower_count'] > data_b['follower_count']
        else:
            return data_a['follower_count'] < data_b['follower_count']

    clear()

    # check user's answer, if user win, call game() with previous data and current score + 1.
    # If user lose, print a message with current score and end the function.
    if check_answer(guess):
        game(data_b, score + 1)
    else:
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")


game()
