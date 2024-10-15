

a, b, c = map(int, input().split())
unique_numbers = {a, b, c}

if len(unique_numbers) == 3:
    # Все числа разные
    print(0)
elif len(unique_numbers) == 2:
    # Два числа одинаковые, одно отличается
    print(2)
else:
    # Все три числа одинаковые
    print(3)
