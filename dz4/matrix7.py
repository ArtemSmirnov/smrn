import random
import numpy
M = random.randrange(2,10)
N = random.randrange(2,10)
K = random.randrange(0,M)
print("M = ",M,"; N = ",N,"; K = ",K)
a = numpy.zeros((M, N))
for i in range(M):
    for j in range(N):
        a[i][j] = random.randrange(-5,5)
print(a)
print("Строка ",K,": ")
print(a[K])
print()
Matrix = [[random.randrange(-5,5) for x in range(N)] for y in range(M)]
print(Matrix)
print("Строка ",K,": ")
print(Matrix[K])
