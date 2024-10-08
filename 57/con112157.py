"""# for 5 
n = 5
numbers = []

for i in range(n):
    a = list(map(int, input().split()))
    numbers.extend(a)

# output min and max
print(min(numbers))
print(max(numbers)) 
"""


a, b, c, d, e = map(int, input().split())

print(min(a, b, c, d, e))
print(max(a, b, c, d, e))

"""

if a > b and a > c and a > d and a > e:
    print("A")
elif b > a and b > c and b > d and b > e:
    print("B")
elif c > a and c > b and c > d and c > e:
    print("C")  
"""

def min_max_and_maximum(numbers):
    # try None 
    if not numbers:
        return None, None, None  

    minimum = min(numbers)
    maximum = max(numbers)

    # определение индекса и числа min и max
    max_value = maximum
    max_index = numbers.index(max_value)

    # return min and max and letters
    letters = [a, b, c, d, e]
    return minimum, maximum, letters[max_index]


for i in range(n):
    a = list(map(int, input().split()))
    numbers.extend(a)

minimum, maximum, max_letter = min_max_and_maximum(numbers)

print(minimum)
print(maximum)
if max_letter:
    print(max_letter)
