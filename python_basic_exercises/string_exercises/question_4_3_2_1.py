# Exercise 4: Arrange string characters such that lowercase letters should come first

def arrange_string(given_string):
    return ''.join(sorted(given_string, key=str.isupper))

# Example usage
input_string = "PyNaTiVe"
output = arrange_string(input_string)
# print(output)

# Exercise 3: Create a new string made of the first, middle, and last characters of each input string

s1="America"
s2="Japan"
s3=""

s3=s3+s1[0]+s2[0]+s1[len(s1)//2]+s2[len(s2)//2]+s1[-1]+s2[-1]
# print(s3)

# Exercise 2: Append new string in the middle of a given string
s1 = "Aulty"
s2 = "Kelly"
s3=''
first_half=s1[0:len(s1)//2]
second_half=s1[len(s1)//2:]
s3=first_half+s2+second_half
# print(s3)

# Exercise 1B: Create a string made of the middle three characters

str1 = "JhonDipPeta"
str1 = "JaSonAy"

print(str1[len(str1)//2-1]+str1[len(str1)//2]+str1[len(str1)//2+1])
