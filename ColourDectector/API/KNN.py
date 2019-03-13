import csv

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

    return 'Prediction!!!'


	