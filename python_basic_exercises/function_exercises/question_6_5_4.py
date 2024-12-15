#recurive function

def addition(num):
    if num:
        return num+addition(num-1)
    else:
        return 0
    
print(addition(10))


# exercise 5
# Exercise 5: Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it

def addition(a,b=3):
    def sum(a,b):return a+b
    return (sum(a,b)+5,1)

print(addition(1))
