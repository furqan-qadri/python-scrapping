# Exercise 5: Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"

int_count=0
str_count=0
other_count=0

for char in str1:
    if char.isalpha():
        str_count+=1
    elif char.isdigit():
        int_count+=1
    else: 
        other_count+=1
    
print(str_count,int_count,other_count)