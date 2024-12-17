# Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
length=2
list3=[]
for i in range(2):
    for j in range(2):
        current_word=list1[i]+list2[j]
        list3.append(current_word)
        
print(list3)

for i in range(2):
    print(i)