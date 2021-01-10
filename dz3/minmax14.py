import random
#N = random.randrange(1,15)
N = 10
print("N = ",N)
B = random.randrange(5,13)
print("B = ",B)
L1 = [random.randint(1, 10) for i in range(N)]
print("Initial:")
print(L1)
L2 = [i for i in L1 if i > B]
print("Processed:")
print(L2)
if len(L2) == 0:
    print("00, больших, чем B, нет")
else:
    x = min(L2)
    print("Минимальное из больших, чем B:",x)
    print("Индекс:",L1.index(x))
				
