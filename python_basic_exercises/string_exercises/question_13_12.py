# Exercise 13: Split a string on hyphens
# str1 = "Emma-is-a-data-scientist"
# str1_list=str1.split("-")
# for item in str1_list:
#     print(item)

# exercise 12:Find the last position of a given substring

#manual implementation
str1 = "Emma is a data scientist who knows Python. Emma works at google."
# str1_array= str1.split(' ')
# position=0
# for i in range(len(str1_array)):
#     if (str1_array[i]=="furqan"):
#         position=position+i
# mm_position=' '.join(str1_array[:position])
# print(len(mm_position)+1)

#using rfind()
position=str1.rfind("Emma")
print(position)
