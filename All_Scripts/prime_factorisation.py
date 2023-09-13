'''
Prime Factorisation : process of writing a number with the product of its prime factors
'''


# function to check if a number is prime or not
def check_prime(number):
    prime = True
    if number in (1, 2):
        return prime
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                prime = False
                break
        return prime

#lengthy solution
def get_prime_factorisation_of_number(number):
    new_num = []
    all_list = []
    if check_prime(number):
        all_list.append(number)
        return all_list
    for i in range(2, number):
        if number % i == 0:
            if check_prime(i):
                new_num.append(i)
    for val in new_num:
        while number % val == 0:
            number = number / val
            all_list.append(val)
    return all_list


# an optimised solution compared to above solution
def prime_fact(n):
    if check_prime(n):
        return [1, n]
    else:
        some = [i for i in range(2, n + 1) if check_prime(i) and n % i == 0]
        all_somelist = []
        for val in some:
            while n % val == 0:
                n /= val
                all_somelist.append(val)
        return all_somelist


print(prime_fact(130))
