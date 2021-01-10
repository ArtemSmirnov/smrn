import random

A = random.randrange(2,10)
A = 7
print('A = ', A)

K = 1.0
S = 1.0
while S+1/(K+1) < A:
    K += 1
    x = 1/K
    S += x
    print("K = {0}, 1/K = {1}, S = {2}".format(K,x,S))

print("K = {0}, S = {1}".format(K,S))
print("K+1 = {0}, S_next = {1}".format(K+1,S+1/(K+1)))
