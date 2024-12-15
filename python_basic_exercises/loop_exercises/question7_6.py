for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print("")
    
# Exercise 6: Count the total number of digits in a number

print(len(str(12345)))

#using while loop
number=834758
count=0
while(number!=0):
    number=number//10
    count+=1
print(count)