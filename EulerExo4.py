l2 = []
c=0
for i in range(100,1000):
    for j in range(100,1000):
        s=j*i
        liste = [int(k) for k in str(s)]
        if liste[::-1]==liste and s>c:
            l2=liste
            c=s
print(l2)