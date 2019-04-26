# Importing the Keras libraries and packages
from keras.models import load_model
model = load_model('Resources/CNNModel/fashionModel.h5')
import numpy as np
# import os
import urllib.request
# import gzip
# import shutil
# import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import *
from PIL import Image
import os

def Test():

    root = Tk()
    # root.filename =  filedialog.askopenfilename()
    root.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",filetypes = (("png files","*.png"),("all files","*.*")))

    url = root.filename
    # for the while loop 
    choice = True
    # this makes sure a file is selcted 
    while choice:
        # check if the file is selected
        if (url.endswith('.jpg')) or (url.endswith('.png')):
            print (root.filename)
            choice = None
        else:
            root.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",filetypes = (("png files","*.png"),("all files","*.*")))
   
    # this is the path if the image 
    Imgpath  = root.filename

    # the label is the name of the image in this case 
    #print("\nThe label of the Image is", unserInput)
    #here the image is converted to grayscale and then numpy array
    img =  Image.open(Imgpath).convert("L")
    img = img.resize((28,28))
    im2arr = np.array(img)
    im2arr = im2arr.reshape(1,28,28,1)

    # Predicting the Test set results
    pred = model.predict(im2arr)
    print(pred)
    correct_indices = np.nonzero(pred > 0.1)
    
    #print("The program predicts image number to be:", correct_indices[-1])
    #print(pred.index(max(pred))
    #print(correct_indices)

    # from the prediction array print the result 
    if correct_indices[-1] == 0:
        print("The program predicts image number to be T-shirt/top")
    elif correct_indices[-1] == 1:
        print("The program predicts image number to be Trouser")
    elif correct_indices[-1] == 2:
        print("The program predicts image number to be Pullover")
    elif correct_indices[-1] == 3:
        print("The program predicts image number to be Dress")
    elif correct_indices[-1] == 4:
        print("The program predicts image number to be Coat")
    elif correct_indices[-1] == 5:
        print("The program predicts image number to be Sandle")
    elif correct_indices[-1] == 6:
        print("The program predicts image number to be Shirt")
    elif correct_indices[-1] == 7:
        print("The program predicts image number to be Sneaker")
    elif correct_indices[-1] == 8:
        print("The program predicts image number to be Bag")
    elif correct_indices[-1] == 9:
        print("The program predicts image number to be Ankle boot")

#https://stackoverflow.com/questions/20443846/python-pil-nameerror-global-name-image-is-not-defined