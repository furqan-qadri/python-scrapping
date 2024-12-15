import math
# Exercise 12: Calculate income tax
# Calculate income tax for the given income by adhering to the rules below

# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
# Expected Output:

# For example, suppose the income is 45000, and the income tax payable is

# 10000*0% + 10000*10%  + 25000*20% = $6000.

def income_tax_calculator(income):
    after_first=income-10000
    if (after_first)<=0:
        return "You have NO tax liability"
    if (after_first)<20000:
        return after_first*0.1
    if (after_first)>=20000:
        tax=1000+(income-20000)*0.2
        return (math.ceil(tax))

print(income_tax_calculator(45000))
    

