l2 = []
for k in range(2,1000000):
    n=k
    liste = [n]
    while n!=1:
        if n%2==0:
            n=n/2
        else :
            n=3*n+1
        liste.append(n)
    if len(liste)>len(l2):
        l2=liste
print(l2[0])