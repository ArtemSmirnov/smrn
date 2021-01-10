def func(b):
    if b>0:
        return b+1
    else:
        return b
    
a = open("data1.txt", "r")
f = open("result1.txt", "w")
f.write(str(func(int(a.read()))))
a.close()
f.close()
