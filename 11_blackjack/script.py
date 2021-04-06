from art import logo
import random
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')



def start():
    hand = []
    for card in range(2):
        hand.append(deal())
    return hand

def deal():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(deck)

def judge(player, dealer, state):

    player_num = sum(player)
    dealer_num = sum(dealer)

    print (f"Your cards: {player}, current score: {player_num}")
    print (f"Computer's first card: {dealer[0]}")

    if player_num > 21 or dealer_num > 21 or state == 'final':
        print (f"Your final hand: {player}, final score: {player_num}")
        print (f"Computer's final hand: {dealer}, final score: {dealer_num}")       

    if player_num > 21:
        print ("You went over. You lose 😭")
        return False
    elif dealer_num > 21:
        print ("Dealer went over. You win 😁")
        return False
    elif state == 'final':
        if dealer_num > player_num:
            print ("You lose 😤")
        elif player_num > dealer_num:
            print ("You win 😃")
        else:
            print ("Draw 🙃")
        return False
    else:
        return True
    

def ace_check(hand):
    while sum(hand) > 21 and 11 in hand:
            index = hand.index(11)
            hand[index] = 1
    return hand


def play_game ():

        print(logo)

        continue_game = True

        player_hand = start()
        dealer_hand = start()

        while continue_game:
            player_hand = ace_check(player_hand)
            dealer_hand = ace_check(dealer_hand)

            continue_game = judge(player_hand,dealer_hand, 'stay')
            
            if not continue_game:
                break

            player_action = input("Type 'y' to get another card, type 'n' to pass: ")
            
            if player_action =='n':
                while sum(dealer_hand) < 16:
                    dealer_hand.append(deal())
                    dealer_hand = ace_check(dealer_hand)
                continue_game = judge(player_hand, dealer_hand, 'final')
            else:
                player_hand.append(deal())
                if sum(dealer_hand) < 16:
                    dealer_hand.append(deal())

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
    clear()
    play_game()
