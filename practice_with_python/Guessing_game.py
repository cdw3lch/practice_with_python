import random

rd = random.randint(1,9)
guess = 0
c = 0
while guess != rd and guess != "exit":
    guess = input("Enter a guess between 1 to 9: ")

    if guess == "exit":
        break

    guess = int(guess)
# this is shorthand for adding 1 to c each time
    c += 1

    if guess < rd:
        print("Too low")
    elif guess > rd:
        print("Too high")
    else:
        print("Right!")
        again = input("\nWould you like to play again? [y/n] ")
        print("You took only", c, "tries!", again)
        if again == "y":
            continue
        else:
            again == "n"
            break








