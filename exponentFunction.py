def power(base,exponent):
    counter = 0 
    output = 1
    while counter < exponent:
        output *= base
        counter += 1
    return output

#------Main Program-------

base = int(raw_input("Enter a base for your power function: "))
exponent = int(raw_input("Enter an exponent for your power function: "))
if exponent != 0:
    final = power(base,exponent)
    print("{}^{} is {}".format(base,exponent,final))
else:
    print("{}^{} is 1".format(base,exponent))