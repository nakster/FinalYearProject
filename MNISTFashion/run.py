# Importing the Keras libraries and packages
from keras.models import load_model
model = load_model('MNISTFashion/fashionModel.h5')
from PIL import Image
import numpy as np
import os
import urllib.request
import gzip
import shutil
import matplotlib.pyplot as plt
from keras.datasets import fashion_mnist

# C:\Users\naqi\Desktop\Django\MNISTFashion\fashionModel.h5
# C:\Users\naqi\Desktop\Django\MNISTFashion\Images
# Load the fashion-mnist pre-shuffled train data and test data
# (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()


# I made the images in gimp 100px * 100px 
# the background needs to be black and the number in white 
# if not it wil not work
# print("\n Enter image file")
# unserInput = input()

def Test():
    # the label is the name of the image in this case 
    #print("\nThe label of the Image is", unserInput)
    #here the image is converted to grayscale and then numpy array
    img = Image.open('MNISTFashion/Images/sa3.png').convert("L")
    img = img.resize((28,28))
    im2arr = np.array(img)
    im2arr = im2arr.reshape(1,28,28,1)


    # Predicting the Test set results
    pred = model.predict(im2arr)
    print(pred)
    correct_indices = np.nonzero(pred)
    print(correct_indices)
    print("The program predicts image number to be:", correct_indices[-1])


Test()