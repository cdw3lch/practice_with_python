print('Welcome to the tip calculator.')
bill = input('What was the total bill? $')
people = input('How many people to split the bill? ')
tip = input('What percentage tip would you like to give? 10, 12 or 15? ')
tip_m = int(tip) / 100 + 1
each = float(bill) * float(tip_m) / int(people)
each = round(each, 2)
each = f'{each:.2f}'
print("Each person should pay: $" + str(each))
