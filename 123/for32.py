for N in range(1,32,5):
    print("N = ",N)
    A0 = 1
    for k in range(1,N+1):
        A1 = (A0 + 1)/k
        print(k," : ",A1)
        A0 = A1
