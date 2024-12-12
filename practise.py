import datetime
import json
import re,os
# print("Hello world")
# x=-12.9999999
# print(type(x))
# y=int(x)
# print(y)
# intro="hello my name is furqan"
# print(intro[-6:])
# print(intro.replace("furqan","******"))
# print("she said \"oh my god. That's amazing\"")

# age=25
# intro=f"My name is furqan and I am {age} years old"
# print(intro)

# print("%.2f"%(20//3))

fruits = ["apple","orange","grapes","banana","papaya"]
# fruits.clear()
# print(fruits)

# for i in range(len(fruits)):
#     print(i)
# i=0  
# while i < (len(fruits)):
#     print(i)
#     i+=1

# print(len([x for x in fruits if "banana" in x]))

# newFruits=list(fruits)
# newFruits=(fruits.copy())
# newFruits=fruits[:]
# print(newFruits.reverse())
# print(newFruits.reverse().sort())
newFruits=list(fruits)

# newFruits=fruits[:]

# print(newFruits)

list1=[1,2,3]
list2=[4,5,6]

'''method 1 using the plus operator
 combinedList= list1+ list2
method 2 using the extend() method
# list1.extend(list2)
 print(list1)
print(combinedList)
'''

# to modify the tuple, convert it to a list, do the modifications and then convert it back to a tuple
cars=('volvo','bmw','merc','suzuki','audi')
carsList=list(cars)
carsList.append("jaguar")
cars=tuple(carsList)
# print(type(cars))

#sets in python
mySet1={1,2,3,4,5,4}
mySet2={6,7,8,3,2}
# for x in range(len(mySet)):
    # print (x)

# mySet.add(6)
# mySet.update(mySet1)
# mySet3= mySet1.union(mySet2)
# mySet3= mySet1.symmetric_difference(mySet2)
# print(mySet3)

#write a function to convert celsius to fahrenheit

# def celcius_to_fahrenheit(temperature):
#     # print(f"Converting {temperature} to fahrenheit...")
#     return 9*temperature/5+32

# celcius_to_fahrenheit = lambda x: 9*x/5+32


# print(celcius_to_fahrenheit(37))

#classes and objects -OOP

# class Person:
#     def __init__(self,name,age,city):
#         self.name=name
#         self.age=age
#         self.city=city
        
#     def __str__(self):
#         return f"Hello! I am {self.name}. I am {self.age} years old and I live in {self.city}"
    
#     def agein2030(self):
#         print(f"My age in 3000 will be {2100-(2024-self.age)} ")

# person1=Person("furqan",25,"Leeds")
# person1.age=24
# print(person1)
# # print(person1.agein2030)
# # person1.agein2030()
# x=datetime.datetime.now() #most imp then do the manipulations
# print(x.strftime("%p"))

# print(f"Copyright {x}")
        




# print(json.dumps(42))


# dictionary and getting all the values and showing all the keys

mydict={
    "name": "Furqan",
    "year": 1,
    "city": "leeds",
    "course":"msc ai",
    "country":"united kingdom",
    "male":True
}

# dictList=(mydict.values())

# print(mydict["name"])
# print(mydict.get("name"))
# add something
mydict["race"]="kashmiri"
# print((mydict.items()))

mydict.update({"country":"united states","city":"san fran","laptop":"macos"})
# print(mydict)

myDictCopy=mydict.copy()
myDictCopy1=dict(mydict)
print(myDictCopy1)

mydictjson=json.dumps(myDictCopy1)

print(mydictjson)


txt="furqan is a good boy"

x=(re.search("furqan",txt))
print("person found") if x else print("not found")


powerchaWinkas= False

print("power chuuuu") if powerchaWinkas else print("pdd'as trath paen")

# list_of_words=[]
# f=open("hello.txt")
# for x in f:
#     list_of_words.append(x)
# print(list_of_words)
# f=open("testing.js")
# print(f.read())
# f.close()

# try:
#     # print(1+"hello")
#     nameList=["areeba"]
#     # for i in range(3):
#     #     name=input("Enter your name : \n")
#     #     nameList.append(name)
#     print(nameList)
#     # city=input("Enter your city : \n")
# except:
#     print("there was an error in the try statement")
# # else:
#     # print(f"Your name is {name} and you live in {city}" )
#         # print(nameList)
# finally:
#     print("---END OF OPERATION---")

try:
    os.remove("hello.txt")
except:
    print(f"yoooo The file does not exist or was already deleted")
    


    
    