print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()
name3 = name1 + name2

fnd_t = name3.count('t')
fnd_r = name3.count('r')
fnd_u = name3.count('u')
fnd_e = name3.count('e')

fnd_l = name3.count('l')
fnd_o = name3.count('o')
fnd_v = name3.count('v')
    
scr1 = str(fnd_t + fnd_r + fnd_u + fnd_e)
scr2 = str(fnd_l + fnd_o + fnd_v + fnd_e)

scr3 = scr1 + scr2
scr3 = int(scr3)

if scr3 in range(0,10):
    print(f"Your score is {scr3}, you go together like coke and mentos.")
elif scr3 in range(40, 50):
    print(f"Your score is {scr3}, you are alright together.")
elif scr3 in range(90,1000):
    print(f"Your score is {scr3}, you go together like coke and mentos.")
else:
    print(f"Your score is {scr3}")

    




