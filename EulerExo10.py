from math import sqrt

s=0
for i in range(2,2000000):
    j=2
    while j<=sqrt(i) and i%j!=0:
        j=j+1
    if j>sqrt(i):
        s=s+i
print(s)