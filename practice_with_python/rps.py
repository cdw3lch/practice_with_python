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

import random

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

comp_choice = random.randint(0, 2)

if player_choice == "0":
    if comp_choice == 0:
        print(f"{rock}")
        print(f"Computer chose:\n {rock} \nIt's a draw!")
    elif comp_choice == 1:
        print(f"{rock}")
        print(f"Computer chose:\n {paper} \nYou lose!")
    else:
        print(f"{rock}")
        print(f"Computer chose:\n {scissors} \nYou win!")



if player_choice == "1":
    if comp_choice == 0:
        print(f"{paper}")
        print(f"Computer chose:\n {rock} \nYou win!")
    elif comp_choice == 1:
        print(f"{paper}")
        print(f"Computer chose:\n {paper} \nIt's a draw!")
    else:
        print(f"{paper}")
        print(f"Computer chose:\n {scissors} \nYou lose!")

if player_choice == "2":
    if comp_choice == 0:
        print(f"{scissors}")
        print(f"Computer chose:\n {rock} \nYou lose")
    elif comp_choice == 1:
        print(f"{scissors}")
        print(f"Computer chose:\n {paper} \nYou win!")
    else:
        print(f"{scissors}")
        print(f"Computer chose:\n {scissors} \nIt's a draw!")
