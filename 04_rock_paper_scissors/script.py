import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock, paper, scissors]
player_num = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors \n'))
computer_num = random.randint(0,2)
if player_num >= 3:
  print('You chose invalid number.')
else:
  print(hands[player_num])
  print('Computer chose:')
  print(hands[computer_num])
  if player_num == computer_num:
    print("You tied.")
  elif (player_num - computer_num) == 1 or (player_num - computer_num) == -2:
    print('You win!')
  else:
    print('You lose.')

