"""Program to test the functions in primes.py"""

import primes as p

first_number = input("Give me a number: ")
second_number = input("Give me another number: ")
factor_string = ""
factor_string_second = ""

if p.check_if_prime(first_number):
    print("\nThe first number you gave me is a prime number.\n")

elif not p.check_if_prime(first_number):
    print("\nThe first number you gave me is not a prime number.")
    factor_list_first = p.identify_factors(first_number)

    for value in factor_list_first:
        if value == factor_list_first[-1]:
            factor_string += f"{value}."
        else:
            factor_string += f"{value}, "

    print(f"Here are the factors of {first_number}: {factor_string}\n")

if p.check_if_prime(second_number):
    print("The second number you gave me is a prime number.\n")

elif not p.check_if_prime(second_number):
    print("The second number you gave me is not a prime number.")
    factor_list_second = p.identify_factors(second_number)

    for value in factor_list_second:
        if value == factor_list_second[-1]:
            factor_string_second += f"{value}."
        else:
            factor_string_second += f"{value}, "

    print(f"Here are the factors of {second_number}: {factor_string_second}\n")

hcf = p.identify_hcf(first_number, second_number)

if type(hcf) == type(factor_string):
    print(hcf)
else:
    print(f"The hcf of those two numbers is {hcf}")
