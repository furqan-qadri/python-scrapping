# Exercise 10: Write a program to count occurrences of all characters within a string

str1="Apple"

#without using count() function

index=0
for i in range (len(str1)):
    char=str1[i]
    place=i
    count=1
    for i in range(len(str1)):
        if str1[i]==char and i!=place:
            count+=1
    print(char,count)

