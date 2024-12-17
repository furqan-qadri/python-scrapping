import json
x="""[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""
data=[]
try:
    data=json.loads(x)
except Exception as e:
    print(e)
print(data)
dataList=[item.get('name') for item in data]
print (dataList)