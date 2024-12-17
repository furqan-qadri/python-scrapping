sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

# remaning a value
# sample_dict["city"]="London"
# print(sample_dict)
sample_dict["location"]=sample_dict.pop("city")
print(sample_dict)