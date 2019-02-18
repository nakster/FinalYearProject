import warnings # current version of seaborn generates a bunch of warnings that will be ignored
warnings.filterwarnings('always')
warnings.filterwarnings('ignore')

# data visualisation and manipulation
import numpy as np # handles mathemathical operations
import pandas as pd # handling data 
import matplotlib.pyplot as plt# plotting graphs 
import seaborn as sns  # handles data visualisation

# load Iris Flower dataset
IrisData = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
# display the first 20 values in the dataset
print(IrisData.head(20))

# Normalize the data
data_norm = IrisData[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].apply(lambda x: (x - x.min()) / (x.max() - x.min()))
print(data_norm.sample(n=5))

# Convert the names of the species setosa','versicolor','virginica to numerical values 
# so it can be easily used for the neural network 
target = IrisData[['species']].replace(['setosa','versicolor','virginica'],[0,1,2])
print(target.sample(n=5))

#add the two datas to make one 
# add the normalised data and the species that are represented by a number now 
data = pd.concat([data_norm, target], axis=1)
print(data.head(5))

# for testing the neural network we going to seperate some 
train_Test = 90/100.0
data['train'] = np.random.rand(len(data)) < train_Test

#from the data seperate the training and testing data
train = data[data.train == 1]
train = train.drop('train', axis=1).sample(frac=1)

#seperate test data
test = data[data.train == 0]
test = test.drop('train', axis=1)

X = train.values[:,:4]
targets = [[1,0,0],[0,1,0],[0,0,1]]
y = np.array([targets[int(x)] for x in train.values[:,4:5]])

#Create backpropagating
# neural network
# inputs is the sepal_length', 'sepal_width', 'petal_length', 'petal_width' of the flower type
inputs = len(X[0])





