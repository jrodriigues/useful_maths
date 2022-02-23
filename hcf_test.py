"""Program that will pass a function to it's simplest form"""

from functions import identify_hcf

numerator = input("Tell me the numerator: ")
denominator = input("Tell the denominator: ")

a = identify_hcf(int(numerator), int(denominator))    # this will give the variable 'a' the highest common factor between the numerator and the denominator

# 'a' can have two types: integer - if there is a HCF between both numbers, or string - if there isn't a HCF between them
if type(a) == type(numerator):   # if 'a' is a string, then we know there isn't a HCF, so the fraction is already in its simplest form
    simplest_fraction = f"{int(numerator)} / {int(denominator)}"

else:
    simplest_fraction = f"{int(int(numerator) / a)} / {int((int(denominator) / a))}"

print(simplest_fraction)