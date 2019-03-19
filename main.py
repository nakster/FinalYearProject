from MongoDB import password as p
from NeuralNetworkScratch import iris
from MNISTFashion import run
from ColourDectector import colourDetect
import cv2
from ColourDectector.API import urlImage

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
             # #C:\Users\naqi\Desktop\Django\ColourDectector 
            image = cv2.imread('ColourDectector/Images/' + userInput + '.jpg')

            colourDetect.predict(image)
            
        #this is to test the image from the url    
        elif choice=="2":

            #we going to read in the url that is going to be tested 
            print("Enter image URL")
            url = input()

            # send the url to the method which converts it
            image = urlImage.urlImage(url)

            colourDetect.predict(image)
            
        # this is to exit the loop
        elif choice=="3":
            print("\n Goodbye") 
            choice = None
        else:
            print("\n Not Valid Choice Try again")

# this is when you are logged in
def logged():
    # this for while loop
    logChoice = True
    # this is a countious while looop
    while logChoice:
         # ask for the options 
        print("""
        ----- Neural Network Menu -----
        1. Run The Iris Preceptron
        2. Run The Fashion MNIST NN
        3. Run The Coulour Detector KNN
        4. Logout 
        """)
        logChoice = input("What would you like to do? ")

        # option 1 handles the neural network made from scratch 
        if logChoice == "1":
            # this here trains the neural network and prints the results 
            iris.TrainIris()
        elif logChoice == "2":
            run.Test()   
        elif logChoice == "3":
            main()
        else:
            logChoice = None

# this is for the methods menu
choice = True
# while loop
while choice:
    # ask for the options 
    print("""
    ----- User Menu -----
    1.Add A User
    2.Login
    3.Update a User
    4.Exit/Quit
    """)
    choice = input("What would you like to do? ")

    # if the user picks one then add a new user 
    if choice=="1":
        p.AddUser()
    # if the user picks 2 log a new user 
    elif choice == "2":
        if p.login() == True:
            print("You have Logged In!")
            # after logging in run the log menu
            logged()      
    # if the user picks 3 update the user 
    elif choice == "3":
        print("Update")
    else:
    # to get out of the while loop
        choice = None 
        print("Bye")



