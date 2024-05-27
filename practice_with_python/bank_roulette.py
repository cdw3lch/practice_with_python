import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
winner = random.choice(names)
print(winner)

