print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

S = 15
M = 20
L = 25
pep_s = 2
pep_ml = 3
xchse = 1

if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            bill = S + pep_s + xchse
            print(f"Your final bill is: ${bill}")
        elif extra_cheese == "N":
            bill = S + pep_s
            print(f"Your final bill is: ${bill}")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill = S + xchse
            print(f"Your final bill is: ${bill}")
        elif extra_cheese == "N":
            bill = S
            print(f"Your final bill is: ${bill}")

if size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            bill = M + pep_ml + xchse
            print(f"Your final bill is: ${bill}")
        elif extra_cheese == "N":
            bill = M + pep_ml
            print(f"Your final bill is: ${bill}")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill = M + xchse
            print(f"Your final bill is: ${bill}")
        elif extra_cheese == "N":
            bill = M
            print(f"Your final bill is: ${bill}")

if size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            bill = L + pep_ml + xchse
            print(f"Your final bill is: ${bill}")
        elif extra_cheese == "N":
            bill = L + pep_ml
            print(f"Your final bill is: ${bill}")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill = L + xchse
            print(f"Your final bill is: ${bill}")
        elif extra_cheese == "N":
            bill = L
            print(f"Your final bill is: ${bill}")
   
