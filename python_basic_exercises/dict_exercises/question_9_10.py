# Write a Python program to change Brad’s salary to 8500 in the following dictionary.
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict["emp3"]["salary"]=8500
# print(sample_dict)

# Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict1 = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

x=sample_dict1.get("Physics")
for key in sample_dict1.values():
    if key<x:
        x=key
print(x)

print(min(sample_dict1, key=sample_dict1.get))