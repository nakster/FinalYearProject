#first install pip install pymongo
#second install pip install dnspython
from pymongo import MongoClient
import gridfs
import cv2
import numpy as np
import matplotlib.pyplot as plt

# access our image collection
# client = MongoClient('localhost', 27017)

# instiallise the connection
# The "dnspython" module must be installed to use mongodb+srv:// URIs
client = MongoClient("mongodb+srv://root:root@cluster0-xyrvy.mongodb.net/test?retryWrites=true")
db = client.MongoProject
testCollection = db.myImageCollection
fs = gridfs.GridFS(db)


def saveImageTocloud(Imgpath):

    print("What name would you like to save the image as: ")
    userInput = input()

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
    

def showImage():

    print("What Image would you like to search from database: ")
    userInput = input()

    # get the image meta data
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

path = './Images/red2.jpg'
# saveImageTocloud(path)
showImage()






























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
