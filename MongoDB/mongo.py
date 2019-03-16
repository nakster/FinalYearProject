#first install pip install pymongo
# import pymongo as mongo
# import gridfs
# import os


from pymongo import MongoClient
import gridfs
import cv2
import numpy as np
import matplotlib.pyplot as plt

# access our image collection
client = MongoClient('localhost', 27017)
db = client['testDatabaseONE']
testCollection = db['myImageCollection']

fs = gridfs.GridFS(db)


# # read the image and convert it to RGB
image = cv2.imread('./yellow.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# convert ndarray to string
imageString = image.tostring()

# store the image
imageID = fs.put(imageString, encoding='utf-8')

# create our image meta data
meta = {
    'name': 'myTestSet',
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

# get the image meta data
image = testCollection.find_one({'name': 'myTestSet'})['images'][0]

# get the image from gridfs
gOut = fs.get(image['imageID'])

# convert bytes to ndarray
img = np.frombuffer(gOut.read(), dtype=np.uint8)

# reshape to match the image size
img = np.reshape(img, image['shape'])


plt.imshow(img) 
plt.show()



























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




