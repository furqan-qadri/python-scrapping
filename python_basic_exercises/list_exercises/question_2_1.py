# Exercise 2: Concatenate two lists index-wise
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# Given:

list1 = ["M", "na", "i", "Ke","and","I","helooo"]
list2 = ["y", "me", "s", "lly","some"]

list3=[]

# custom implementation without zip function
min_length= min(len(list1),len(list2))
for i in range(min_length):
    current_word=list1[i]+list2[i]
    list3.append(current_word)
list3.extend(list1[min_length:] or list2[min_length:])
print(list3)

# using zip function
list4= [i+j for i,j in zip(list1,list2)]
list4.extend(list1[min_length:] or list2[min_length:])
print(list4)
