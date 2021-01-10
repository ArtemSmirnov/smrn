import random
import math

def IsSquare(K):
    x = int(math.sqrt(K))
    if K == x*x:
        return True
    return False

s = 0
for i in range(0,10):
    x = random.randrange(1,101)
    print(x,end="; ")
    s += int(IsSquare(x))

print("\nКоличество квадратов:",s)
