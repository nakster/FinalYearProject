# import tensorflow as tf
# import keras 
# from keras.callbacks import TensorBoard
# import numpy as np 
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.optimizers import Adam
from keras.utils import np_utils
from keras.datasets import fashion_mnist

# Load the fashion-mnist pre-shuffled train data and test data
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

print("x_train shape:", x_train.shape, "y_train shape:", y_train.shape)

# Show one of the images from the training dataset
# img_index = 3
# plt.imshow(x_train[img_index])
# plt.show()


# Reshaping to format which CNN expects (batch, height, width, channels)
x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1).astype('float32')
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1).astype('float32')



#Data normalization
#We then normalize the data dimensions so that they are of approximately the same scale.
# normalize inputs from 0-255 to 0-1
x_train/=255
x_test/=255


# convert class vectors to binary class matrices
#number of classes
classes = 10
# one-hot encoding
# we are expecting output as 8 means value of output variable 8
# so according to one-hot coding its [0,0,0,0,0,0,0,0,1,0]
y_train = np_utils.to_categorical(y_train, classes)
y_test = np_utils.to_categorical(y_test, classes)



#Define the model
model = Sequential()
# Must define the input shape in the first layer of the neural network
model.add(Conv2D(filters=64, kernel_size=2, padding='same', activation='relu', input_shape=(28,28,1))) 
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.3))

model.add(Conv2D(filters=32, kernel_size=2, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(classes, activation='softmax'))
# Take a look at the model summary
model.summary()

#Compile the model

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])


#Fit the model
model.fit(x_train,y_train, batch_size=64, epochs=10,validation_data=(x_test, y_test))

# Save the model to use test the pictures for later
model.save('fashionModel.h5')

# Evaluate the model on test set
score = model.evaluate(x_test, y_test, verbose=0)
# Print test accuracy
print("Metrics(Test lo ss & Test Accuracy): ")
print('Test loss:', score[0])
print('Test accuracy:', score[1])


