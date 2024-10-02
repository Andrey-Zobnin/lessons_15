"""con112148.py"""
import random

a, b = map(float, input().split())

random_numbers = [random.uniform(a, b) for _ in range(5)]

"""
fors = []  

for num in random_numbers:  # Проходим по каждому числу в списке random_numbers
    fors = f"{num:.3f}"  # Форматируем 
    fors.append(fors)  

"""
fors = [f"{num:.3f}" for num in random_numbers]

print(" ".join(fors))
