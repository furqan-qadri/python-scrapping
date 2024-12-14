# Exercise 13: Print multiplication table from 1 to 10

def multiplication_table(number):
    for i in range(1,number+1):
        for j in range(1,11):
            print(i*j, end=" ")
        print("")
         
multiplication_table(100)
