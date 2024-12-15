# str1 = 'I am 25 ye5ars and 10 months old'
# print("Original string is", str1)

# # Retain Numbers in String
# # Using list comprehension + join() + isdigit()
# res = "".join([item for item in str1 if item.isdigit()])

# print(res)
#using filter
str1="phone h1ow are you 123"
# filter_numbers=''.join(filter(str.isdigit,str1))
# print(filter_numbers)

#using list comprehension
filter_numbers=''.join([item for item in str1 if item.isdigit()])
print(filter_numbers)