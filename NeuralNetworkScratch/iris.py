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
df_norm = IrisData[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].apply(lambda x: (x - x.min()) / (x.max() - x.min()))
print(df_norm.sample(n=5))
