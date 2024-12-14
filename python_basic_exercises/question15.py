# Exercise 15: Get an int value of base raises to the power of exponent
# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

def raised_value(number,exp):
    for i in range(exp):
        number=number*number
        return number

print(raised_value(6,2))