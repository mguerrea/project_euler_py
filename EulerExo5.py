from math import factorial

c =0

for n in range (1, factorial(20)) :
    for i in range (1,21) :
        if n%i == 0 :
            c = c+1
    if c== 20 :
        print(n)
    c=0

