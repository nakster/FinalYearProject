import os
import os.path
import cv2
import matplotlib.pyplot as plt
from API import KNN as classifier 
from API import prepareTestImage as prepare
from API import urlImage
import requests


def predict(image):

    # Variables
    # read the data file
    # this is the path to the data training file
    dataPath = './Data/training.data'
    testPath = './Data/test.data'
    prediction = ''
    #test if the path is correct
    # print(data)

    # os.path.isfile(path)
    # Return True if path is an existing regular file. 
    # This follows symbolic links, so both islink() and isfile() can be true for the same path.
    # https://docs.python.org/2/library/os.path.html
    if os.path.isfile(dataPath) and os.access(dataPath, os.R_OK):
        print ('The Data File Exists!')
    else:
        print('Data File Does Not Exist!')

    # this here is prepares the image to be tested 
    # changes the test.data file to the rgb values of the image that is going to be tested 
    prepare.prepareImage(image)

    # training the data 
    prediction = classifier.main(dataPath, testPath)

    # print the prediction 
    print('The KNN predicts the Image to be: ' + prediction)

    # Plot the image that we are going to test on 
    # https://matplotlib.org/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure
    plt.figure("The Image to be Tested " + prediction)
    # fixed color distortion error
    # https://stackoverflow.com/questions/37795874/matplotlib-imshow-why-is-img-color-distorted    
    plt.imshow(image[..., ::-1]) 
    plt.show()




def main():

    #make a countinous while loop 
    choice = True

    #ask for 
    while choice:
        print("""
        ----- Colour Detector Menu -----
        1.Test A Image from Image Folder
        2.Test a Image url(must be http and jpg)
        3.Exit/Quit
        """)
        choice = input("What would you like to do? ")

        #first choice is if we select a image from the image folder
        if choice=="1":

            #we going to read in the image that is going to be tested 
            print("Enter image (saved as colors e.g. black)")
            userInput = input()

             #this here reads the image in 
            image = cv2.imread('./Images/' + userInput + '.jpg')

            predict(image)
            

        #this is to test the image from the url    
        elif choice=="2":

            #we going to read in the url that is going to be tested 
            print("Enter image URL")
            url = input()

            # send the url to the method which converts it
            image = urlImage.urlImage(url)

            predict(image)
            
        # this is to exit the loop
        elif choice=="3":
            print("\n Goodbye") 
            choice = None
        else:
            print("\n Not Valid Choice Try again")

#run the main method 
main()

# links 
# https://stackoverflow.com/questions/3388223/python-difference-between-os-access-and-os-path-exists
# https://stackoverflow.com/questions/35286540/display-an-image-with-python
# https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
# http://www.tayloredmktg.com/rgb/