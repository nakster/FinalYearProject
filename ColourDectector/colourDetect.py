import os
import os.path
import cv2
import matplotlib.pyplot as plt
from API import KNN as classifier 
from API import prepareTestImage as prepare
from PIL import Image
# import the necessary packages
import numpy as np
import urllib

def main():
    #we going to read in the image that is going to be tested 
    print("Enter image (saved as colors e.g. black)")
    userInput = input()



    resp = urllib.request.urlopen(userInput)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # response = requests.get(userInput)
    # image = Image.open(BytesIO(response.content))

    # image = Image.open(StringIO(urllib.requests.urlopen(userInput).read()))
    #this here reads the image in 
    # image = cv2.imread('./Images/' + userInput + '.jpg')
    # image = cv2.imread(img)
    plt.imshow(image[..., ::-1]) 
    plt.show()


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

#run the main method 
main()

# links 
# https://stackoverflow.com/questions/3388223/python-difference-between-os-access-and-os-path-exists
# https://stackoverflow.com/questions/35286540/display-an-image-with-python
# https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
# http://www.tayloredmktg.com/rgb/