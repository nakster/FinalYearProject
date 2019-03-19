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
 

def AddUser():

    print("-----Adding a User To Database-----")
    print("What is your User Name: ")
    username = input()
   
    if collection.find_one({'user': username}) == None:
        print("What is your Password: ")
        password = input()

        hashPassword = hash_password(password)
        print(hashPassword)

        # insert the user and password
        # https://stackoverflow.com/questions/31499804/insert-data-into-with-pymongo-and-flask
        collection.insert_one({'user': username, 'password': hashPassword})
    else:
        print("Sorry User Already Exist with Same Name!!")
        print("Try Again")
    

def login():

    print("What is your User Name: ")
    username = input()

    print("What is your Password: ")
    password = input()

    # db = collection.find_one({'user': username})
    db = collection.find_one({'user': username}, {'password': 1, '_id' : 0})
    print(db['password'])

    mongoHash = db['password']

    if check_password(mongoHash,password):
        print('You entered the right password')
    else:
        print('I am sorry but the password does not match')



choice = True

while choice:
    print("""
    ----- User Menu -----
    1.Add A User
    2.Login
    3.Update a User
    3.Exit/Quit
    """)
    choice = input("What would you like to do? ")

    if choice=="1":
        AddUser()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Update")
    else:
        choice = None 
        print("Bye")





# Links
# https://www.pythoncentral.io/hashing-strings-with-python/
