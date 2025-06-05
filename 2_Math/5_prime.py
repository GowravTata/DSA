

def check_prime(n):
    if n in (1,2,3):
        return False
    if n%2 ==0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n % (i+2)==0:
            return False
        i+=6
    return True

print(check_prime(289))

# Python program to print all Primes Smaller
# than or equal to N using Sieve of Eratosthenes


def SieveOfEratosthenes(num):
	prime = [True for i in range(num+1)]
	p = 2
	while (p * p <= num):

		if (prime[p] == True):

			for i in range(p * p, num+1, p):
				prime[i] = False
		p += 1

	for p in range(2, num+1):
		if prime[p]:
			print(p)


# Driver code
if __name__ == '__main__':
	num = 50
	print("Following are the prime numbers smaller"),
	print("than or equal to", num)
	SieveOfEratosthenes(num)
