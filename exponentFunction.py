def power(base,exponent):
    """Takes a number and raises it to another power"""
    if exponent == 0:
        return 1
    else:
        final = base * power(base, exponent - 1)
    return final

def int_input(value):
    """Uses try except to turn user input into an int"""
    number = raw_input(value)
    notInt = True
    while notInt == True:
        try:
            number = int(number)
        except ValueError:
            number = raw_input("Sorry that is not a integer, try again: ")
        else:
            notInt = False
    return number
    
def float_input(value): 
    """Uses try except to turn user input into a float"""
    number = raw_input(value)
    notFloat = True
    while notFloat == True:
        try:
            number = float(number)
        except ValueError:
            number = raw_input("Sorry that is not a number, try again: ")
        else:
            notFloat = False
    return number     
        
#------Test Cases-------

print("2 to the 3rd power is: {}".format(power(2,3)))
print("5 to the 4th power is: {}".format(power(5,4)))
print("8 to the 0 power is: {}".format(power(8,0)))
print("0 to the 4th power is: {}".format(power(0,4)))

#-----Main Program------
base = float_input("Enter the base of the number: ")
exponent = int_input("Enter an integer for the exponent: ")


print("{} to the {} power is: {}".format(base, exponent, power(base,exponent)))


