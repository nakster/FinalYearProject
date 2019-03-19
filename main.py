from MongoDB import password as p



def logged():
    logChoice = True

    while logChoice:
         # ask for the options 
        print("""
        ----- Neural Network Menu -----
        1. Run The Iris Preceptron
        2. Run The Fashion MNIST NN
        3. Run The Coulour Detector KNN
        4.Exit/Quit
        """)
        logChoice = input("What would you like to do? ")

        if logChoice == "1":
            print("choice 1")
        elif logChoice == "1":
            print("choice 2")
        elif logChoice == "1":
            print("choice 3")
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