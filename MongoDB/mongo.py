#first install pip install pymongo
import pymongo as mongo

client = mongo.MongoClient("mongodb://localhost:27017/")
print(client)


