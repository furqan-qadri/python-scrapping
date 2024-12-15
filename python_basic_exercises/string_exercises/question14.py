# Exercise 14: Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

str_modified=[item for item in str_list if item] #since empty strings and None are falsy values
# print(str_modified)

# using filter
str_modified=list(filter(None,str_list))
print(str_modified)