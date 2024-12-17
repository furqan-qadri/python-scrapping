list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list comprehension
list2=[x for x in list1 if x]
print(list2)

# using filter
list3=list(filter(None,list1))
print(list3)


# exercise 5:Exercise 5: Iterate both lists simultaneously
# todo if length is not same then put stars in empty spaces
list5 = [10, 20, 30, 40]
list6 = [100, 200, 300, 400]
length=4
list6.reverse()
for i in range(length):
    print(list5[i],list6[i])
