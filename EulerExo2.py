u0,u1,s = 1,2,2
u = u0+u1
while u < 4000000 :
    u = u0 + u1
    u0 = u1
    u1 = u
    if u%2 == 0 :
        s =s+u
print(s)