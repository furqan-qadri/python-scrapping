# Exercise 1: Convert the following dictionary into JSON format
import json
# data = {"key1" : "value1", "key2" : "value2"}

# x=json.dumps(data)
# print((x))

# Exercise 2: Access the value of key2 from the following JSON
# import json

# sampleJson = """{"key1": "value1", "key2": "value2"}"""
# x=json.loads(sampleJson)
# print(x["key2"])

# Exercise 3: PrettyPrint following JSON data
# PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").

sampleJson3 = {"key1": "value1", "key2": "value2"}
x=json.dumps(sampleJson3,indent=2, separators=(","," = "))
print(x)