
month = int(input())

if month == 12 or month in [1, 2]:
    print("winter")
elif month in [3, 4, 5]:
    print("spring")
elif month in [6, 7, 8]:
    print("summer")
elif month in [9, 10, 11]:
    print("autumn")
else:
    print("NO")
