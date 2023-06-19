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

print("Welcome to Rock, Paper, Scisors!")
player_hand = int(input("Type 0 for ROCK, 1 for PAPER, and 2 for SCISORS:"))

computer_hand = random.randint(0,2)

if player_hand == 0:
    print(f"You chose ROCK!\n{rock}")
elif player_hand == 1:
    print(f"You chose PAPER!\n{paper}")
else:
    print(f"You chose SCISSORS!\n{scissors}")

if computer_hand == 0:
    print(f"Computer chose ROCK!\n{rock}")
elif computer_hand == 1:
    print(f"Computer chose PAPER!\n{paper}")
else:
    print(f"Computer chose SCISSORS!\n{scissors}")

if player_hand == computer_hand:
    print("It's a draw!")
elif (player_hand == 0 and computer_hand == 1) or (player_hand == 1 and computer_hand == 2) or (player_hand == 2 and computer_hand == 0):
    print("Computer Wins!")
else:
    print("You Win!")