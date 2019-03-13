import os
import os.path
import cv2
import matplotlib.pyplot as plt

def main():
    #we going to read in the image that is going to be tested 
    print("Enter image (saved as colors e.g. black)")
    userInput = input()

    #this here reads the image in 
    image = cv2.imread('./Images/' + userInput + '.jpg')

    # Plot the image that we are going to test on 
    plt.figure("The Image to be Tested")
    plt.imshow(image) 
    plt.show()

    # read the data file
    # this is the path to the data training file
    dataPath = './Data/training.data'
    #test if the path is correct
    # print(data)

    # os.path.isfile(path)
    # Return True if path is an existing regular file. 
    # This follows symbolic links, so both islink() and isfile() can be true for the same path.
    # https://docs.python.org/2/library/os.path.html
    if os.path.isfile(dataPath) and os.access(dataPath, os.R_OK):
        print ('The data file exists!')
    else:
        print('There is no data file to train')

#run the main method 
main()
















# links 
# https://stackoverflow.com/questions/3388223/python-difference-between-os-access-and-os-path-exists
# https://stackoverflow.com/questions/35286540/display-an-image-with-python