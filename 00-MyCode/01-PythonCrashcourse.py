import numpy as np

print('xc')

a = [1, 2, 3]
a.append(4)
print(a)


for num in range(0, 2):
    print('Hello {}'.format(num))

list(range(10))
# 0-9 (10 elements)

# list comprehension
x = [1, 2, 3, 4]
out = [num**2 for num in x]
print(out)

# functions


def square(num):
    """
    THIS IS A DOCSTRING
    CAN GO MULTIPLE LINES
    """
    return num**2

# Map and lambda


def times2(var): return var * 2


print(times2(2))
print(list(map(times2, [1, 2, 3])))

# Lambda
# tx = lambda w, q: w*q
# multi line
print(list(map(lambda num: num*3, [1, 2, 3])))
print(list(filter(lambda e: e % 2 != 0, [1, 2, 3, 4])))

# Dictionary
d = {'k1': 1, 'k2': 2}
d.keys()
print('x' in ['x', 'y', 'z'])

xy = [(1, 2), (3, 4), (5, 6)]
for x, y in xy:
    print(x+y)

# Classes


class Test:
    def __init__(self, x, y):
        self.name = x
        self.age = y


t1 = Test('name', 123)
print(t1)
