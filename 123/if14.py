import random

A = random.randrange(-3,3)
B = random.randrange(-3,3)
C = random.randrange(-3,3)

print("Число A:", A)
print("Число B:", B)
print("Число C:", C)

if A < B:
    mn1 = A
    mx1 = B
else:
    mn1 = B
    mx1 = A

if mx1 < C:
    mx1 = C

if mn1 > C:
    mn1 = C    
       
print("Минимум:", mn1)
print("Максимум:", mx1)
