# sum from 1 to n
# number=int(input())
# sum=0
# for i in range(number+1):
#     sum=sum+i
# print(sum)

# Exercise 2: Print the following pattern
# Write a Python code to print the following number pattern using a loop.

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

for i in range(1,6,1):
    for j in range(1,i+1):
        print(j,end="")
    print("")

