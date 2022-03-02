import csv
from functions import check_if_prime

filename = 'list_of_50_primes.csv'

with open(filename) as f:
    reader = csv.reader(f)
    
    row = next(reader)
    
    for value in row:
        number = int(value.strip())
        
        # If check_if_prime returns() 'True', then the number is a prime number; if it returns 'False', then it is not.
        if check_if_prime(number):                                      
            print(f"{number} is prime.")
        
        else:
            print(f"{number} is not a prime.")
