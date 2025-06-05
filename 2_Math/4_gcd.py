
a=96
b=73

while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
# print(a)

def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

print(gcd(24,27))

