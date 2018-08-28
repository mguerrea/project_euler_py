n=1
for i in range(1,101):
    n=n*i
liste = [int(i) for i in str(n)]
s = sum(liste)
print(s)