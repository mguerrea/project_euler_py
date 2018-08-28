s1, s2 = 0,0

for i in range(0,101):
    s1 = s1 + i**2
for j in range(0,101):
    s2 = s2 + j
print(s2)
s2 = s2**2
print(s1)
print(s2)
s3 = s2-s1
print(s3)
