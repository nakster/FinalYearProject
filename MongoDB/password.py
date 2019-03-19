# imports 
from pymongo import MongoClient
import hashlib
import uuid
import re

# connecto to mongodb
client = MongoClient("mongodb+srv://root:root@cluster0-xyrvy.mongodb.net/test?retryWrites=true")
# tell which database you would like to use
db = client.User
# name of the collection
collection = db.passwords

# hash the password 
def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

# check the password entered with the saved password  
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
 
#add a user def
def AddUser():

    #ask the user their name
    print("-----Adding a User To Database-----")
    print("What is your User Name: ")
    username = input()
    # check if the user name doesnt already exists 
    if collection.find_one({'user': username}) == None:
        # if it doesnt then ask for password 
        print("What is your Password: ")
        password = input()

        # save the hash of the password 
        hashPassword = hash_password(password)

        # insert the user and password
        # https://stackoverflow.com/questions/31499804/insert-data-into-with-pymongo-and-flask
        collection.insert_one({'user': username, 'password': hashPassword})
    else:
        # if the user already exists then ask to add new user again
        print("Sorry User Already Exist with Same Name!!")
        print("Try Again")
    
# log a user 
def login():

    # ask for their name 
    print("What is your User Name: ")
    username = input()

    # check if the user name doesnt already exists 
    if collection.find_one({'user': username}) == None:
        # if the user already exists then ask to add new user again
        print("Sorry User Does Not Exists!")
        print("Try Again")
    else:
        # ask the user for password
        print("What is your Password: ")
        password = input()
        # get the password back from the database 
        # db = collection.find_one({'user': username})
        db = collection.find_one({'user': username}, {'password': 1, '_id' : 0})
        # save the password into a new variable 
        mongoHash = db['password']
        #check if the password is the same 
        if check_password(mongoHash,password):
            print('You entered the right password')
        else:
            print('I am sorry but the password does not match')

# Links
# https://www.pythoncentral.io/hashing-strings-with-python/
