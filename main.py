import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["data"]

mydata = [
    {"name": "rakib", "email": "rakib@gmail.com"},
    {"name": "emon", "email": "emon@gmail.com"},
    {"name": "shakil", "email": "shakil@gmail.com"},
    {"name": "tamim", "email": "tamim@gmail.com"},
    {"name": "tusher", "email": "tusher@gmail.com"},
    {"name": "fahim", "email": "fahim@gmail.com"}
]

for x in mydata:
    print(x)

