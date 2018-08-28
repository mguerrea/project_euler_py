from math import sqrt,floor
n = 600851475143
for i in range (1,floor(sqrt(n))):
    if n%i == 0 :
        j = 2
        while j <= floor(sqrt(i)) and i%j!=0:
            j = j+1
        if j > floor(sqrt(i)):
            prem = i
print (prem)