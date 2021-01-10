import math

N = 200
print("N = ",N)
L = []
for x in range(2,N+1):
    n = math.sqrt(x)
    i = 2
    k = 0
    while i <= n:
        if int(x / i)*i == x:
            k += 1
            break
        i += 1
    if k == 0:
        L.append(x)
print(L)
