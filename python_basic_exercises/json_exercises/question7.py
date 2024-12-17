# Exercise 7: Convert the following JSON into Vehicle Object
# { "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }
# For example, we should be able to access Vehicle Object using the dot operator like this.

# vehicleObj.name, vehicleObj.engine, vehicleObj.price

import json

x='''{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }'''
y=json.loads(x)
print(y)
