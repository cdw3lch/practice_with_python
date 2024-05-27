number = input("Enter a number: ")
try:
    if number % 2 == 0:
        print('You have picked an even number')
    else:
        print('You have picked an odd number')
except:
    number = float(number)
    print("Pick a whole number")
    