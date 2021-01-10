num = [[1,2,4,-3],[4,5,7,-6],[7,0,8,-9]]
n = len(num)
num = list(zip(*num))
if all(i < 0 for i in num[-1])  :
    tmp = [0 for i in range(n)]
    num.append(tmp)
num = list(zip(*num))
print(num)
