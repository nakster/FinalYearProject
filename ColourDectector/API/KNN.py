import csv
import math
import operator

# Load image feature data to training feature vectors and test feature vector
def loadDataset(trainingFile,testFile,trainDataFeatureVector=[],testDatFeatureVector=[]):
    # we open the file training.data as traindata
    with open(trainingFile) as traindata:
        # then we read each line 
        read = csv.reader(traindata)
        # the data that is read in memory is added to a new variable called
        data = list(read)
        # print(data)

        #https://stackoverflow.com/questions/1712227/how-to-get-the-number-of-elements-in-a-list-in-python
        # print(len(data))
        # run the for loop the length times of the file 
        for i in range(len(data)):
            # i is the number of times the loop has run
            # we runa secend loop 3 times to add the 3 values to the trainDataFeatureVector
            # ie 139,0,0,red the data looks something like this
            # this is then inside the second loop is seperated into 3 values 
            # i.e 139 0 0
            for j in range(3):
                data[i][j] = float(data[i][j])
            # the seperated data is then added to the trainDataFeatureVector array
            trainDataFeatureVector.append(data[i])
            # print(data[i]) # test to see if everything prints

     # we open the file test.data as testData
    with open(testFile) as testData:
        # read the file here
        read = csv.reader(testData)
        # save the read file as a array
        testSet = list(read)
        # for loop the saved array 
        for i in range(len(testSet)):
            # we runa secend loop 3 times to add the 3 values to the trainDataFeatureVector
            # ie 139,0,0,red the data looks something like this
            # this is then inside the second loop is seperated into 3 values 
            # i.e 139 0 0
            for j in range(3):
                testSet[i][j] = float(testSet[i][j])
            # the seperated data is then added to the testDatFeatureVector array
            testDatFeatureVector.append(testSet[i])


# similarity
# In order to make predictions we need to 
# calculate the similarity between any two given data instances.
# If this distance is small, it will be the high degree of similarity
#  where large distance will be the low degree of similarity.
# The Euclidean distance between two points is the length of the 
# path connecting them.The Pythagorean theorem gives this distance between two points.
def euclideanDistance(instance1, instance2, length):
	distance = 0
    # measure the diference between the two points 
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)


# Neighbors
# After getting the similarty method 
# we can use it to get the K most similar instace for a 
# gievn unseen instance
def getNeighbors(trainDataFeatureVector, testInstance, k):
    # here we will calculate the distance for
    # All instances and select a subset 
    # with the smallest distance values
    distances = []

    # the testInstance is [5.0, 5.0, 5.0]
    # which has a lenth of 3 
    length = len(testInstance) - 1
    
    #run the loop for the length of the trainging data 67 times
    for x in range(len(trainDataFeatureVector)):

        # get the distance of each point 
        # ie [139.0, 0.0, 0.0, 'red'] which is trainDataFeatureVector[1]
        dist = euclideanDistance(testInstance,trainDataFeatureVector[x], length)
        # then append the distance to the trainDataFeatureVector array
        distances.append((trainDataFeatureVector[x], dist))

    # sort the array so we get the smallest distance value at the top
    distances.sort(key=operator.itemgetter(1))
    neighbors = []

    ##this runs 7 times 
    # it gets the first 7 sorted vales from the array distances 
    # appends it to neighbors and returns it 
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

# response of neighbors 
def response(neighbors):
    # array to store all the possible neigbors 
    allNeighbors = {}

    # run the loop len of neighbors which is the class votes i.e red black blue ......
    for x in range(len(neighbors)):
        # response is equal to the last vlaue of each point
        # [9.0, 0.0, 0.0, 'black']
        # ie in the above case its black
        response = neighbors[x][-1]

        # this here checks for each response and counts them up
        # for example red = 2 time and white = 4 times
        # this means the input is more likely to be white 
        if response in allNeighbors:
            #counter
            allNeighbors[response] += 1
        else:
            #counter
            allNeighbors[response] = 1
            
    # this sorts the allNeighbors to have the 
    # for exapmle red = 2 time and white = 4 times
    # this makes sure that the bigger value is first
    sortedVotes = sorted(allNeighbors.items(),key=operator.itemgetter(1), reverse=True)
    #return the first value i.e name of colour 
    return sortedVotes[0][0]


def main(trainData, testData):
    # As we would need to in any machine learning problem,
    # We must first find a way to represent data points as feature vectors.
    # A feature vector is our mathematical representation of data, 
    # and since the desired characteristics of our data may not be inherently numerical,
    # preprocessing and feature-engineering may be required in order to create these vectors
    # https://www.kdnuggets.com/2018/03/introduction-k-nearest-neighbors.html
    trainDataFeatureVector = []
    testDatFeatureVector = []

    #this here loads the training and testing data into memeory and saves it to 
    # trainDataFeatureVector array and testDatFeatureVector array
    loadDataset(trainData, testData, trainDataFeatureVector, testDatFeatureVector)

    ##this array will store the prediction
    prediction = []
    # with a given K value we can make boundaries of each class
    # https://www.analyticsvidhya.com/blog/2018/03/introduction-k-neighbours-algorithm-clustering/
    k = 3

    #run the for loop len(testDatFeatureVector) amount of times 
    for i in range(len(testDatFeatureVector)):
        # https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
        # Locate k most similar data instances.
       
        # getNeigbours 
        neighbors = getNeighbors(trainDataFeatureVector, testDatFeatureVector[i], k)
        # get response 
        res = response(neighbors)
        # append the response to prediction array
        prediction.append(res)
        
    # return the prediction  
    # print(prediction[0])  
    return prediction[0]


	