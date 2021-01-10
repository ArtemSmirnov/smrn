import random
import math

def IsPowerN(K,N):
    x = int(round(math.log(K,N)))
    if K == N**x:
        return True
    return False

def IsPowerNa(K,N):
    while K > 1:
        K /= N
    if K == 1.0:
        return True
    return False

s = 0
s2 = 0
N = random.randrange(2,10)
print("N = ",N)
L = [N**random.randrange(1,10)+random.randrange(0,2) for i in range(0,10)]
for i in range(0,len(L)):
    x = L[i]
    #print(x,end="; ")
    s += int(IsPowerN(x,N))
    s2 += int(IsPowerNa(x,N))
    print(x,":",IsPowerN(x,N),":",IsPowerNa(x,N))

print("\nКоличество от  IsPowerN:",s)
print("\nКоличество от  IsPowerN:",s2)
