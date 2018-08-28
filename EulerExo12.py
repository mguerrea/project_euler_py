from math import floor, sqrt

liste = []
n=0
s=0
while len(liste)<500:
    n=n+1
    s=s+n
    liste = []
    for k in range(1,floor(sqrt(s))):
        if s%k==0:
            liste.append(k)
            liste.append(int(s/k))
print(n)
print(liste)