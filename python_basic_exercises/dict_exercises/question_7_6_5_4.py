# sample_dict = {'a': 100, 'b': 200, 'c': 300}

# for 200 in sample_dict.values():
#         print("True")

# Exercise 6: Delete a list of keys from a dictionary
# Given:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# # Keys to remove
to_remove_keys = ["name", "salary"]
# Expected output:

# {'city': 'New york', 'age': 25}
# normal way
for key in to_remove_keys:
    sample_dict.pop(key)
print(sample_dict)

# dictionary comprehension
sample_dict={k:v for k,v in sample_dict.items() if k not in to_remove_keys}
print(sample_dict)

mydict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
new_dict=[]

new_dict={k:mydict[k] for k in keys}
print(new_dict)