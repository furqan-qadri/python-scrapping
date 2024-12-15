# str1 = "PYnative29@#8496"

# sum=0
# count=0
# for char in str1:
#     if char.isdigit():
#         sum=sum+ int(char)
#         count+=1
# print(sum, sum/count)

# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case

#use the count mehthod

# Exercise 7: String characters balance Test

# s1="Yn"

def string_balancer(s1, s2):
    # Convert strings to sets of characters
    set1 = set(s1.lower())
    set2 = set(s2.lower())
    return set1==set2

# Example inputs
s1 = "PYnative"
s2 = "nativePy"

# Test the function
print(string_balancer(s1, s2))  # Output: True
