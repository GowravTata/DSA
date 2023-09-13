# assumption : input number is always positve and greater than zero

def check_prime_1(number):
    is_prime = True
    if number==1:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        return is_prime


# checkforprime
def check_prime_2(number):
    return False if number==1 else not(any(number % i == 0 for i in range(2, number)))


# optimal solution for larger numbers
def check_prime_3(number):
    prime = True
    if number==1:
        return False
    else:
        # as every number will have a divisor which is less than or equal to it's square root,
        # range can be minimised considering that
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                prime = False
                break
        return prime
