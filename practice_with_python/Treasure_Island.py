print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Welcome to Treasure Island.\nYour mission is to find the treasure.')
choice_1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" ').lower()
if choice_1 == "left":
    print('You\'ve come to a lake. There is an island in the middle of the lake.  ')
    choice_2 = input('Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if choice_2 == "swim":
        print("You get attacked by an angry trout. Game Over.")
    elif choice_2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
        choice_3 = input("Which color do you choose? ").lower()
        if choice_3 == "red":
            print("Burned by fire. Game over")
        elif choice_3 == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("Eaten by beasts. Game over")
elif choice_1 == "right":
    print("You fell into a hole. Game Over.")

    
