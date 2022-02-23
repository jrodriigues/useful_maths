"""Program that identifies prime numbers or factors of composite numbers"""

first_number = input("Give me a number: ")
second_number = input("Give me another number: ")
factor_string = ""
factor_string_second = ""

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

if check_if_prime(first_number):
    print("\nThe first number you gave me is a prime number.\n")

elif not check_if_prime(first_number):
    print("\nThe first number you gave me is not a prime number.")
    factor_list_first = identify_factors(first_number)

    for value in factor_list_first:
        if value == factor_list_first[-1]:
            factor_string += f"{value}."
        else:
            factor_string += f"{value}, "

    print(f"Here are the factors of {first_number}: {factor_string}\n")

if check_if_prime(second_number):
    print("The second number you gave me is a prime number.\n")

elif not check_if_prime(second_number):
    print("The second number you gave me is not a prime number.")
    factor_list_second = identify_factors(second_number)

    for value in factor_list_second:
        if value == factor_list_second[-1]:
            factor_string_second += f"{value}."
        else:
            factor_string_second += f"{value}, "

    print(f"Here are the factors of {second_number}: {factor_string_second}\n")

hcf = identify_hcf(first_number, second_number)

if type(hcf) == type(factor_string):
    print(hcf)
else:
    print(f"The hcf of those two numbers is {hcf}")




