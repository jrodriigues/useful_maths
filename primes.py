"""Functions that identify prime numbers, factors of composite numbers, LCM or HCF of two numbers"""

def check_if_prime(number):
    """Function that checks if this number is a prime number. Returns True or False"""
    is_prime = True

    for value in range(2, int(number)):
        if int(number) % value == 1:
            continue
        elif int(number) % value == 0:
            is_prime = False
            break
    
    return is_prime

def identify_factors(number):
    """Function that identifies all the factors of a number and returns them in a list"""
    factors = []

    for value in range(1, int(number) + 1):
        if int(number) % value == 0:
            factors.append(value)
    return factors

def identify_hcf(first, second):
    """Function that identifies the Highest Common Factor of two numbers. Returns the HCF or string in no HCF is found"""
    first_factors = identify_factors(first)
    second_factors = identify_factors(second)
    first_factors.reverse()
    
    for value in first_factors:
        if value in second_factors:
            if value == 1:
                break
            return value
        
    return f"Sorry, but there are no common factors in these two numbers."



