# Asympototic Analysis (Theoretical Analysis) : Mainly measure order of growth 
"""
For the first function as seen , it runs constant no matter what the input so for this the equation can 
be written as c1
"""
def fun1(n):
    return n*(n+1)//2

"""
For the second function as seen , the constants are assigned are sum, a loop is running n times based on the input given so here the equation written as follows
c2 * n + c3
"""

def fun2(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum

"""
For the second function as seen , the constants are assigned are sum, a loop is running n times based on the input given  and there is another loop which is given n times as per the inner loop so here the equation written as follows
c6 * n2 + c5 * n + c4
"""

def fun3(n):
    sum=0
    for i in range(1,n+1):
        for j in range(i):
            sum=sum+1
    return sum

value=5
print(fun1(value))
print(fun2(value))
print(fun3(value))

