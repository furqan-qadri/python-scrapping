# Exercise 14: Print a downward half-pyramid pattern of stars
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

def pattern(number):
    for i in range(number,0,-1):
        for j in range(i):
            print("*",end="")
        print("")
        
pattern(8)