# Exercise 9: Find the largest item from a given list
def find_highest_number(given_array):
    highest_number=given_array[0]
    for i in range(len(given_array)-1):
        if given_array[i+1]>given_array[i]:
            highest_number=given_array[i+1]
    print(highest_number)

given_array=[4, 6,8, 24, 12, 2,48]
find_highest_number(given_array)

# using array sort
given_array.sort()
print(given_array[-1])

#using built-in max
print(max(given_array))