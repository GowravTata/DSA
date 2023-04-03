# find a solution to print all the divisors of a number

# naive approach

n=729
#for i in range(1,n+1):
#    if n%i==0:
#        print(i)

# a little optimisation than to the above one
# as every number will have divisors in the number of pairs
# Eg: for 36 it is  [(1,36),(2,18),(3,12),(4,9),(6,6)] , so the first number is always less
# than or less than the square root of the number, considering that, below logic was written
for i in range(1, int(n**0.5)+1):
    if n%i==0:
        print(i)
        # this condition is introduced to not to display the same number twice as perfect
        # squares would have
        if n/i!=i:
            print(n/i)


# the above was an optimal solution , but it doesn't print the numbers in a sorted order
# in order to print the numbers in a sorted manner, two loops were written.

i = 1
while i ** 2 < n:
    if n % i == 0:
        print(i)
    i += 1
while i >= 1:
    if n % i == 0:
        print(n / i)
    i -= 1

