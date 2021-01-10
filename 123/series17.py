import random

B = random.randrange(1,10)
print("B = ",B)
N = random.randrange(1,10)
print("N = ",N)

for i in range(1,N+1):
    print(i,end="; ")

print()
flag = True
for i in range(1,N+1):
    print(i,end="; ")
    if i <= B and B <= i+1 and flag:
        print("B:",B,end="; ")
        flag = False
