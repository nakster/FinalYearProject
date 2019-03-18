#first install pip install pymongo
#second install pip install dnspython
from pymongo import MongoClient
import gridfs
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import *
from API import urlImage
import os
# from .ColourDetectector.API import urlImage
# access our image collection
# client = MongoClient('localhost', 27017)

# instiallise the connection
# The "dnspython" module must be installed to use mongodb+srv:// URIs
client = MongoClient("mongodb+srv://root:root@cluster0-xyrvy.mongodb.net/test?retryWrites=true")
db = client.MongoProject
testCollection = db.myImageCollection
fs = gridfs.GridFS(db)


def saveImageTocloud():

    #https://stackoverflow.com/questions/39261178/how-can-tkinter-open-with-file-directory-of-specific-folder-also-containing-py
    root = Tk()
    # root.filename =  filedialog.askopenfilename()
    root.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

    # for the while loop 
    choice = True
    # this makes sure a file is selcted 
    while choice:
        # check if the file is selected
        if "jpg" in root.filename:
            print("Its A Jpg file!!")
            print (root.filename)
            choice = None
        else:
            root.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
   
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
        print("No Image Found With This Name!")

def SaveUrlImage():

    # ask the user for url
    print("Please Enter the Image Url: ")
    url = input()

    check = True
    # this checks if the correct url is 
    while check:
        #check if the string ends with .png or jpg
        # https://www.programiz.com/python-programming/methods/string/endswith
        if (url.endswith('.jpg')) or (url.endswith('.png')):
            print("The image is in the correct format")
            check = None
        else:
            #if it doesnt end with the following then ask agian
            print("Please Enter the Image Url: ")
            url = input()

    # convert to cv2 type 
    img = urlImage.urlImage(url)

    #ask for th name
    print("What name would you like to save the image as: ")
    userInput = input()

    try:
        testCollection.find_one({'name': userInput})['images'][0]
        print("Sorry Image Already Exist with Same Name!!")
        print("Try Again")
    except:
        print("Searched Database Name is unique Adding to database!!")
        # convert ndarray to string
        imageString = img.tostring()

        # store the image
        imageID = fs.put(imageString, encoding='utf-8')

        # create our image meta data
        meta = {
            'name': userInput,
            'images': [
                {
                    'imageID': imageID,
                    'shape': img.shape,
                    'dtype': str(img.dtype)
                }
            ]
        }

        # insert the meta data
        testCollection.insert_one(meta)
        print("Image Added To database")


SaveUrlImage()
# saveImageTocloud()
# showImage()


### #####################################
# https://stackoverflow.com/questions/53682647/mongodb-atlas-authentication-failed-on-python
# https://pythonspot.com/tk-file-dialogs/
