numbers = [1, 2, 3, 4, 5, 6, 7]

numbers1=[x*x for x in numbers] #list comprehension
print(numbers1)

# traditional looping 
numbers2=[]
for number in numbers:
    numbers2.append(number*number)
print(numbers2)

#using map
numbers3=list(map(lambda x:x*x,numbers))
print(numbers3)