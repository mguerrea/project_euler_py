#from math import sqrt,floor
p=0
for a in range(1,1000):
    for b in range(a,1000):
        for c in range(b,1000):
            if c**2==b**2+a**2:
                if a+b+c==1000:
                    p = a*b*c
print(p)