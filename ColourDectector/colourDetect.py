import os
import os.path
import matplotlib.pyplot as plt
from API import KNN as classifier 

def main():
    #we going to read in the image that is going to be tested 
    print("Enter image (saved as colors e.g. black)")
    userInput = input()

    #this here reads the image in 
    image = cv2.imread('./Images/' + userInput + '.jpg')

    # Plot the image that we are going to test on 
    # https://matplotlib.org/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure
    plt.figure("The Image to be Tested")
    plt.imshow(image) 
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


    #check if testing data exists
    if os.path.isfile(dataPath) and os.access(dataPath, os.R_OK):
        print ('The Test Data File Exists!')
    else:
        print('Test Data File Does Not Exist!')


    # training the data 
    prediction = classifier.main(dataPath, testPath)

    # print the prediction 
    print(prediction)

#run the main method 
main()
















# links 
# https://stackoverflow.com/questions/3388223/python-difference-between-os-access-and-os-path-exists
# https://stackoverflow.com/questions/35286540/display-an-image-with-python