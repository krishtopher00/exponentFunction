# Author: Krish Bhavnani
# Date: March 9, 2016

def power(base,exponent):
    # To loop and multiply the base by itself a certain number of times
    counter = 0 
    # Need a starting value of 1 to properly account for each multiplication
    output = 1
    while counter < exponent:
        output *= base
        counter += 1
    return output

#------Main Program-------

base = int(raw_input("Enter a base for your power function: "))
exponent = int(raw_input("Enter an exponent for your power function: "))
# Anything to the 0 power is 1!
if exponent != 0:
    final = power(base,exponent)
    print("{}^{} is {}".format(base,exponent,final))
else:
    print("{}^{} is 1".format(base,exponent))