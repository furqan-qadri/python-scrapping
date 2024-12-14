# #Given two lists of numbers, write a Python code to create a new list such that the latest list should contain odd numbers from the first list and even numbers from the second list.

# # additions:
# #if list has a repetition of a number make sure it is not there in the final array
# #if any of the arrays contains anything other a number then return immediately 

def odd_even_list(list1,list2):
    odd_even_list=[]
    for i in set(list1):
        try:
            if (i%2!=0):
                odd_even_list.append(i)
        except:
                return "List1 contains non numerical value"
        
    for i in set(list2):
        try:
            if (i%2==0):
                odd_even_list.append(i)
        except TypeError:
                return "List2 contains non numerical value"   
    return odd_even_list

list1 = [1,1,1,1,1,1,1,1,1,2,3]
list2 = [1,40,45, 60, 75, 90,-2]

# print(odd_even_list(list1,list2))
print(odd_even_list(list1,list2))


# l1 = [2,5,8,12,4,6,87,32,65]
# l2 = [1,6,3,90,4,5,32,4]

#list comprehension- without checking for 
odd_even_unique_list=([n for n in set(list1) if n%2]+[n for n in set(list2) if not n%2])
print(odd_even_unique_list)

list1=[1,2,3,4,5,6,7,8,9]

even_numbers=[n for n in list1 if n%2==0]
print(even_numbers)
