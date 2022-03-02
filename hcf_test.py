"""Program that will pass a fraction to it's simplest form"""

from functions import Maths

NUMERATOR = input("Tell me the numerator: ")
DENOMINATOR = input("Tell the denominator: ")

request = Maths(NUMERATOR, DENOMINATOR)

# This will give the variable 'hcf' the highest common factor between the numerator and the denominator

hcf = request.identify_hcf(int(NUMERATOR), int(DENOMINATOR))

# 'hcf' can have two types: integer - if there is a HCF between both numbers, or string - if there isn't a HCF between them
# if 'a' is a string, then we know there isn't a HCF, so the fraction is already in its simplest form

if type(hcf) == type(NUMERATOR):
    simplest_fraction = f"{int(NUMERATOR)} / {int(DENOMINATOR)}"

else:
    simplest_fraction = f"{int(int(NUMERATOR) / hcf)} / {int((int(DENOMINATOR) / hcf))}"

print(simplest_fraction)