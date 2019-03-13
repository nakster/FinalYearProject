import os
import os.path
import cv2
import matplotlib.pyplot as plt


#we going to read in the image that is going to be tested 
print("Enter image (saved as colors e.g. black)")
userInput = input()

#this here reads the image in 
image = cv2.imread('./Images/' + userInput + '.jpg')

# Plot the image that we are going to test on 
plt.figure("The Image to be Tested")
plt.imshow(image) 
plt.show()
















# links 
# https://stackoverflow.com/questions/3388223/python-difference-between-os-access-and-os-path-exists
# https://stackoverflow.com/questions/35286540/display-an-image-with-python