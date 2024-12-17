list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list comprehension
list2=[x for x in list1 if x]
# print(list2)

# using filter
list3=list(filter(None,list1))
# print(list3)


# exercise 5:Exercise 5: Iterate both lists simultaneously
# ToDo if length is not same then put stars in empty spaces
list5 = [10, 20, 30, 40,60]
list6 = [100, 200, 300, 400,70,80,90,99,800,900]
list6.reverse()
length=(min(len(list5),len(list6)))
for i in range(length):
    print(list5[i],list6[i])
print(*list5[len(list6):] or list6[len(list5):], sep="\n")

print(*[1,2,3,4,5])