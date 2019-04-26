import cv2
import numpy as np

def prepareImage(img):

    # load the image
    image = img
    #https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_basic_ops/py_basic_ops.html
    chans = cv2.split(image)

    #declare variables 
    colors = ('b', 'g', 'r')
    features = []
    feature_data = ''
    counter = 0

    # foor loop to calculate the rgb of the image 
    for (chan, color) in zip(chans, colors):
        counter = counter + 1
        #calculate the rgb
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        features.extend(hist)

        # find the peak pixel values for R, G, and B
        elem = np.argmax(hist)

        if counter == 1:
            blue = str(elem)
        elif counter == 2:
            green = str(elem)
        elif counter == 3:
            red = str(elem)
            feature_data = red + ',' + green + ',' + blue
            # print(feature_data)

    #here open the test.data file and right the rgb value which will be tested with the knn
    with open('KNearestNeighbors/Data/test.data', 'w') as myfile:
        myfile.write(feature_data) 

# links
# https://www.programiz.com/python-programming/methods/built-in/zip