import warnings # current version of seaborn generates a bunch of warnings that will be ignored
warnings.filterwarnings('always')
warnings.filterwarnings('ignore')

# data visualisation and manipulation
import numpy as np # handles mathemathical operations
import pandas as pd # handling data 
import matplotlib.pyplot as plt# plotting graphs 
import seaborn as sns  # handles data visualisation
from sklearn import preprocessing

# load Iris Flower dataset
IrisData = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
# display the first 20 values in the dataset
# print(IrisData.head(20))

# Normalize the data
data_norm = IrisData[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].apply(lambda x: (x - x.min()) / (x.max() - x.min()))
# print(data_norm.sample(n=5))

# Convert the names of the species setosa','versicolor','virginica to numerical values 
# so it can be easily used for the neural network 
target = IrisData[['species']].replace(['setosa','versicolor','virginica'],[0,1,2])
# print(target.sample(n=5))

#add the two datas to make one 
# add the normalised data and the species that are represented by a number now 
data = pd.concat([data_norm, target], axis=1)
# print(data.head(5))

# for testing the neural network we going to seperate some 
train_Test = 90/100.0
data['train'] = np.random.rand(len(data)) < train_Test

#from the data seperate the training and testing data
train = data[data.train == 1]
train = train.drop('train', axis=1).sample(frac=1)

#seperate test data
test = data[data.train == 0]
test = test.drop('train', axis=1)

# x is basically the trainig data without the id number and species column 
X = train.values[:,:4]
targets = [[1,0,0],[0,1,0],[0,0,1]]
# y replaces the species position 
# i.e if in the train data array if the specie is 1 which is setosa
# then the y target is given that position
# for example number 1 is setosa this means the target array would look like 
# [1 0 0] so 1 represents the correct position of the species
y = np.array([targets[int(x)] for x in train.values[:,4:5]])

#Create backpropagating
# neural network
# inputs is the sepal_length', 'sepal_width', 'petal_length', 'petal_width' of the flower type
inputs = len(X[0]) # len is 4
hiddenLayer = 5

#"A random seed is a number used to initialize a pseudorandom number generator."
np.random.seed(4)

# weight 1 is the matrices of weight connecting the input and the hiddenLayer
# input layer nodes connect with hidden layer nodes
weight1 = 2*np.random.random((inputs, hiddenLayer)) - 1

# make a connection between hidden layer and output i.e weights 2 do that
output = len(y[0]) # len is 3 
weight2 = 2*np.random.random((hiddenLayer, output)) - 1

##### Train  the neural network

# slowly update the network
learning_rate = 0.2 
for epoch in range(50000):
    #sigmoid activation function squashes the input values between 0 and 1. 
    #This provides a consistant way for the network to deal with outputs.
    layer1 = 1/(1 + np.exp(-(np.dot(X, weight1)))) # sigmoid function
    layer2 = 1/(1 + np.exp(-(np.dot(layer1, weight2))))
    er = (abs(y - layer2)).mean()
    layer2_delta = (y - layer2)*(layer2 * (1-layer2))
    layer1_delta = layer2_delta.dot(weight2.T) * (layer1 * (1-layer1))
    weight2 += layer1.T.dot(layer2_delta) * learning_rate
    weight1 += X.T.dot(layer1_delta) * learning_rate
print('Error Rate for prediction is:', er)

#testX is aarray without the id and the species column
testX = test.values[:,:4]
# testY replaces the species position 
# i.e if in the train data array if the specie is 1 which is setosa
# then the y target is given that position
# for example number 1 is setosa this means the target array would look like 
# [1 0 0] so 1 represents the correct position of the species
testY = np.array([targets[int(x)] for x in test.values[:,4:5]])

l1 = 1/(1 + np.exp(-(np.dot(testX, weight1))))
l2 = 1/(1 + np.exp(-(np.dot(l1, weight2))))

np.round(l2,3)


yp = np.argmax(l2, axis=1) # prediction
res = yp == np.argmax(testY, axis=1)
correct = np.sum(res)/len(res)

testres = test[['species']].replace([0,1,2], ['setosa','versicolor','virginica'])
print(testres)

testres['Prediction'] = yp
testres['Prediction'] = testres['Prediction'].replace([0,1,2], ['setosa','versicolor','virginica'])

print(testres)
print('Correct:',sum(res),'/',len(res), ':', (correct*100),'%')

