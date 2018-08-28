from math import floor, sqrt

l3 = []

for i in range (1,10001):
    #print(i)
    l1 = [1]
    l2 = [1]
    for k in range(2, floor(sqrt(i))):
        if i%k==0:
            l1.append(k)
            l1.append(i/k)
    j = sum(l1)
    #print(j)
    for m in range(2,floor(sqrt(j))):
        if j%m==0:
            l2.append(m)
            l2.append(j/m)
    n = sum(l2)
    #print(n)
    if j!=n :
        if n==i and j not in l3:
            l3.append(j)
        if n==i and i not in l3:
            l3.append(i)
    #print(l3)

print(sum(l3))
