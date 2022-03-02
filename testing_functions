"""Program to test the functions in primes.py"""

from functions import Maths

# Gets the input from the user to create the object
FIRST_NUMBER = input("Give me a number: ")
SECOND_NUMBER = input("Give me another number: ")

# Support variables in case the HCF method returns a string type
first_factor_string = ""
second_factor_string = ""

request = Maths(FIRST_NUMBER, SECOND_NUMBER)


# Check for if both numbers are prime. If not, return their factors.

if request.check_if_prime(FIRST_NUMBER):
    print("\nThe first number you gave me is a prime number.\n")

elif not request.check_if_prime(FIRST_NUMBER):
    print("\nThe first number you gave me is not a prime number.")
    factor_list_first = request.identify_factors(FIRST_NUMBER)

    # Allows a neatly formatted string to be returned
    for value in factor_list_first:
        if value == factor_list_first[-1]:
            first_factor_string += f"{value}."
        else:
            first_factor_string += f"{value}, "

    print(f"Here are the factors of {FIRST_NUMBER}: {first_factor_string}\n")

if request.check_if_prime(SECOND_NUMBER):
    print("The second number you gave me is a prime number.\n")

elif not request.check_if_prime(SECOND_NUMBER):
    print("The second number you gave me is not a prime number.")
    factor_list_second = request.identify_factors(SECOND_NUMBER)

    # Allows a neatly formatted string to be returned
    for value in factor_list_second:
        if value == factor_list_second[-1]:
            second_factor_string += f"{value}."
        else:
            second_factor_string += f"{value}, "

    print(f"Here are the factors of {SECOND_NUMBER}: {second_factor_string}\n")

hcf = request.identify_hcf(FIRST_NUMBER, SECOND_NUMBER)

# Compares the type of both variables: the below condition is 'True', then 'hcf' == str type, therefore there are no common factors.

if type(hcf) == type(first_factor_string):
    print(hcf)
else:
    print(f"The hcf of those two numbers is {hcf}")

# Retrieves the Lowest Common 

lcm = request.identify_lcm(FIRST_NUMBER, SECOND_NUMBER)

# Compares the type of both variables: the below condition is 'True', then 'lcm' == str type, therefore there are no common multiples found.

if type(lcm) == type(first_factor_string):
    print(lcm)
else:
    print(f"The lcm of those two numbers is {lcm}")