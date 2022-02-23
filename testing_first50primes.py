from numpy import number
from functions import check_if_prime
import csv

with open('list_of_50_primes.csv') as f:
    reader = csv.reader(f)
    
    row = next(reader)
    
    for value in row:
        number = int(value.strip())
        
        if check_if_prime(number):
            print(f"{number} is prime.")
        
        else:
            print(f"{number} is not a prime.")
