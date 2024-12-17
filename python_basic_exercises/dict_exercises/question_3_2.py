sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict["class"]["student"]["marks"]["history"])
dict1={'a':2, 'b':4, 'c':10}


dict4 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict5 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict6={**dict4,**dict5}
print(dict6)