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

#Write your code below this line 👇
import random

options_list = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

print(options_list[player_choice])
print("Computer chose:\n")
print(options_list[computer_choice])

if player_choice == computer_choice:
    print("It's a draw!")
elif player_choice == 0 and computer_choice == 1:
    print("Computer wins!")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 1 and computer_choice == 0:
    print("You win!")
elif player_choice == 1 and computer_choice == 2:
    print("Computer wins!")
elif player_choice == 2 and computer_choice == 0:
    print("Computer wins!")
elif player_choice == 2 and computer_choice == 1:
    print("You win!")