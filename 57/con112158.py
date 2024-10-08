
"""
num_0, num_1, num_2 = map(int, input().split())

if max(num_0, num_1, num_2) == num_0:
    print("A")
elif max(num_0, num_1, num_2) == num_1:
    print("B")
elif max(num_0, num_1, num_2) == num_2:
    print("C")
"""
"""
a, b, c = map(int, input().split())
if a > b and a > c:
    print("A")
elif b > a and b > c:
    print("B")
elif c > a and c > b:
    print("C")
elif a == b and a > c:
    print("A B")
elif b == c and b > a:
    print("B C")
elif a == c and a > b:
    print("A C")
elif a == c and c == b and b == a:
    print(0)

"""

a, b, c = map(int, input().split())


# проверка на максимум
if a > b and a > c:
    print("A")
elif b > a and b > c:
    print("B")
elif c > a and c > b:
    print("C")

# проверка на минимум
if a < b and a < c:
    print("A")
elif b < a and b < c:
    print("B")
elif c < a and c < b:
    print("C")
