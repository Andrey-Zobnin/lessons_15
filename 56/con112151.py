import random
a, b = map(int, input().split())


random_numbers = [random.randint(a, b) for _ in range(5)]

print(" ".join(map(str, random_numbers)))

