import random

N = random.randrange(1,10)
print("N = ",N)

x = random.randrange(1,10)
print(x,end="; ")
x_prev = x
k = 0
for i in range(1,N):
    x = random.randrange(1,10)
    if x < x_prev:
        k += 1
        print("*{0}".format(x),end="; ")
    else:
        print(x,end="; ")
    x_prev = x
print()
print("K = ",k)
