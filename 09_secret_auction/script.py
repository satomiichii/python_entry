from art import logo
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

bid = {}
continue_bid = True

print(logo)

while continue_bid:
    name = input ('What is your name?: ')
    price = int(input('What is your bid: $'))
    bid[name] = price
    add_bid = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if add_bid == 'no':
        continue_bid = False
    elif add_bid == 'yes':
        clear()
    else:
        print('Your input is invalid.')

max_name = ''
max_bid = 0

for name in bid:
    price = bid[name]
    if price > max_bid:
        max_bid = price
        max_name = name

print (f"The winner is {max_name} with a bid of ${max_bid}")