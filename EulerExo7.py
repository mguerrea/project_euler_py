from math import sqrt
i = 2
liste = []
while len(liste)<10001 :
    j=2
    while j<=sqrt(i) and i%j!=0 :
        j = j+1
    if j>sqrt(i) :
        liste.append(i)
    i = i+1
print(liste[10000])
print(len(liste))