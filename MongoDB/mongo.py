#first install pip install pymongo
#second install pip install dnspython
from pymongo import MongoClient
import gridfs
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import *
# from tkinter.filedialog import askopenfilename

# access our image collection
# client = MongoClient('localhost', 27017)

# instiallise the connection
# The "dnspython" module must be installed to use mongodb+srv:// URIs
client = MongoClient("mongodb+srv://root:root@cluster0-xyrvy.mongodb.net/test?retryWrites=true")
db = client.MongoProject
testCollection = db.myImageCollection
fs = gridfs.GridFS(db)


def saveImageTocloud():

    root = Tk()
    # root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    root.filename =  filedialog.askopenfilename()
    print (root.filename)
    
    # this is the path if the image 
    Imgpath  = root.filename

    print("What name would you like to save the image as: ")
    userInput = input()

    try:
        testCollection.find_one({'name': userInput})['images'][0]
        print("Sorry Image Already Exist with Same Name!!")
        print("Try Again")
    except:
        print("Searched Database Name is unique Adding to database!!")

        # # read the image and convert it to RGB
        image = cv2.imread(Imgpath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # convert ndarray to string
        imageString = image.tostring()

        # store the image
        imageID = fs.put(imageString, encoding='utf-8')

        # create our image meta data
        meta = {
            'name': userInput,
            'images': [
                {
                    'imageID': imageID,
                    'shape': image.shape,
                    'dtype': str(image.dtype)
                }
            ]
        }

        # insert the meta data
        testCollection.insert_one(meta)
        print("Image Added To database")
    

def showImage():

    print("What Image would you like to search from database: ")
    userInput = input()

    # get the image meta data
    try:
        image = testCollection.find_one({'name': userInput})['images'][0]
         # get the image from gridfs
        gOut = fs.get(image['imageID'])

        # convert bytes to ndarray
        img = np.frombuffer(gOut.read(), dtype=np.uint8)

        # reshape to match the image size
        img = np.reshape(img, image['shape'])

        # display the image 
        plt.imshow(img) 
        plt.show()
    except:
        print("none")

path = './Images/red2.jpg'
saveImageTocloud()
# showImage()






























# db = mongo.MongoClient().gridfs_example
# fs = gridfs.GridFS(db)


# print(os.path.getsize( r'yellow.jpg' ))

# # f = fs.open("hello.txt", "w")
# fileID = fs.put( open( r'yellow.jpg', 'rb'))

# out = fs.get(fileID)

# print(out)


# client = mongo.MongoClient("mongodb://localhost:27017/")

# mydb = client["mydatabase"]
# mydb = mydb["images"]


# print(os.path.getsize( r'yellow.jpg' ))

# fs = gridfs.GridFS(mydb)
# fileID = fs.put( open( r'yellow.jpg', 'rb'))

# out = fs.get(fileID)

# for x in mydb.find():
#   print(x)



### #####################################
# https://stackoverflow.com/questions/53682647/mongodb-atlas-authentication-failed-on-python
# https://pythonspot.com/tk-file-dialogs/
