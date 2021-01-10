import random

A = random.randrange(-3,3)
B = random.randrange(-3,3)
C = random.randrange(-3,3)
print("Три числа:", A, B, C)

x = 0
if A > 0:
    x += 1
if B > 0:
    x += 1
if C > 0:
    x += 1
print("Количество положительных чисел: ", x)

y = 0
if A < 0:
    y += 1
if B < 0:
    y += 1
if C < 0:
    y += 1
print("Количество отрицательных чисел: ", y)
