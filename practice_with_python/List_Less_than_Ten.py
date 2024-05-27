a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lsthn = []

for num in a:
    if num < 5:
        lsthn.append(num)
        lsthn.sort()
print(lsthn)
