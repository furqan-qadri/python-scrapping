# Exercise 10: Remove all occurrences of a specific item from a list.

# list1 = [5, 20, 15, 20, 25, 50, 20]
# for number in list1:
#     if number==20:
#         list1.remove(number)
# print(list1)

# # list comprehension
# list2=[x for x in list1 if x!=20]
# print(list2)


# Exercise 9: Replace list’s item with new value if found

list1 = [5, 10, 15, 20, 25, 50, 20]

# for i in range(len(list1)):
#     if list1[i]==20:
#         list1[i]=200
#         break
# print(list1)

# to learn-enumerate and index
for i,var in enumerate(list1):
    if var==20:
        list1[i]=200
print(list1)
        


