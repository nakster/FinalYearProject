from NeuralNetworkScratch.iris import TrainIris
from MNISTFashion.run import Test

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
            TrainIris()
        elif logChoice == "2":
            Test()   
        elif logChoice == "3":
            print("choice 3")
        else:
            logChoice = None

