"""Functions that identify prime numbers, factors of composite numbers, 
   Lowest Common Multiples or Highest Common Factors of two numbers,
   All belonging to the class Maths"""


class Maths():
    """Class that will allow the creation of objects containing two numbers."""

    def __init__(self, first, second):
        """Method to initialize the objects with two numbers"""
        self.first = first
        self.second = second

    def check_if_prime(self, number):
        """Function that checks if this number is a prime number. 
        Returns True or False"""

        is_prime = True

        for value in range(2, int(number)):
            if int(number) % value == 1:
                continue
            elif int(number) % value == 0:
                is_prime = False
                break
        
        return is_prime

    def identify_factors(self, number):
        """Function that identifies all the factors of a number and returns them in a list"""

        factors = []

        for value in range(1, int(number) + 1):
            if int(number) % value == 0:
                factors.append(value)
        return factors

    def identify_hcf(self, first, second):
        """Function that identifies the Highest Common Factor of two numbers. 
        Returns the HCF or string in no HCF is found"""

        first_factors = self.identify_factors(first)
        second_factors = self.identify_factors(second)
        first_factors.reverse()
        
        for value in first_factors:
            if value in second_factors:
                if value == 1:
                    break
                return value
            
        return f"Sorry, but there are no common factors in these two numbers."

    def identify_lcm(self, first, second):
        """Function that identifies the Lowest Common Multiple of two numbers.
        Returns the integer LCM or string if no LCM is found"""
        
        first_multiples = []
        second_multiples = []

        for number in range(1, 1000000):
            first_multiple = int(first) * number
            first_multiples.append(first_multiple)

        for number in range(1, 1000000):
            second_multiple = int(second) * number
            second_multiples.append(second_multiple)
        
        for value in first_multiples:
            if value in second_multiples:
                return value
        
        return f"No LCM found."



