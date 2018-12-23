#!/usr/bin/env python
# coding: utf-8

# # Using Tensorflow to predict values of a function,
# based on previous functions
#
# **Authors:** Wladymir Brborich, Jean Karlo Obando, Miguel Guaño,
# Christopher Rojas
#
# ## Considerations
#
# This project mostly an empirical aproach to aproximate function values,
# the base for the code and nn architecture where taken from this
#  [article](https://medium.com/mlreview/a-simple-deep-learning-model-for-
# stock-price-prediction-using-tensorflow-30505541d877),
# whith this [repo](https://github.com/sebastianheinz/stockprediction),
#  feel free to check them out
#
# ## Tools used
#
# ### Tensorflow
#
# It is an open source library for machine learning, ideal to start coding and
# building your own neural networks, [more info](https://www.tensorflow.org/)
#
# ### Pandas
#
# Pandas is the most popular data analysis tool on python,
# learn more [here](https://pandas.pydata.org/)
#
# ## Building the model
#
# First we need to import our dependecies

# In[ ]:


import pandas as pd
import tensorflow as tf
import numpy as np


# We will use code from p5.js function map() to scale our data set

# In[ ]:


def translate(n, start1, stop1, start2, stop2):
    return ((n-start1)/(stop1-start1))*(stop2-start2)+start2


# Then we create a dataset from an excel sheet with the values for training

# In[ ]:


data = pd.read_excel('training_data.xlsx', 'Training')
data.head()


# Then for the values for predicting the function

# In[ ]:


data_testing = pd.read_excel('training_data.xlsx', 'Predicting')
data_testing.head()


# After we can separate our training and testing data,
# this is to evolve our neural network

# In[ ]:


n = data.shape[0]
data = data.values
testing_percentage = 0.9

train_start = 0
train_end = int(np.floor(testing_percentage*n))
test_start = train_end
test_end = n
data_train = data[np.arange(train_start, train_end), :]
data_test = data[np.arange(test_start, test_end), :]

n = len(data_train[0])
print(n)

print(data_train)
print(data_test)


# We also convert our testing data to the apropiate format

# In[ ]:


data_testing = data_testing.values
print(data_testing)


# We separate the input data, from the known answers or outputs, for each set

# In[ ]:


x_train = data_train[:, 0:n-1]
print('Training set')
print(x_train)
y_train = data_train[:, n-1]
print(y_train)
print('Testing set')
x_test = data_test[:, 0:n-1]
print(x_test)
y_test = data_test[:, n-1]
print(y_test)


# We scale our sets to the range (-1, 1) so we can
# feed those data into the neural network

# In[ ]:


x_train = np.array([[translate(item, 8, 20, -1, 1)
                     for item in col] for col in x_train])
print(x_train)
y_train = np.array([translate(item, 8, 20, -1, 1) for item in y_train])
print(y_train)


# In[ ]:


x_test = np.array([[translate(item, 8, 20, -1, 1)
                    for item in col] for col in x_test])
print(x_test)
y_test = np.array([translate(item, 8, 20, -1, 1) for item in y_test])
print(y_test)


# In[ ]:


data_pred = np.array([translate(item, 8, 20, -1, 1) for item in data_testing])
print(data_pred)


# We then define our neural network architecture, we use a lot of neurons
# with 4 layers to converge into a suitable prediction faster,
# with not to many itterations

# In[ ]:


n_prices = x_train.shape[1]
# Neurons
n_neurons_1 = 1024
n_neurons_2 = 512
n_neurons_3 = 256
n_neurons_4 = 128


# Then we declare our Tensorflow stuff, mainly our tensors,
# in which we pass the data arrays

# In[ ]:


net = tf.InteractiveSession()
# Placeholder
X = tf.placeholder(dtype=tf.float32, shape=[None, n_prices])
Y = tf.placeholder(dtype=tf.float32, shape=[None])


# After that, we build the neural network
#
# 1. inicialize weights and biases

# In[ ]:


sigma = 1
weight_initializer = tf.variance_scaling_initializer(
    mode="fan_avg", distribution="uniform", scale=sigma)
bias_initializer = tf.zeros_initializer()

W_hidden_1 = tf.Variable(weight_initializer([n_prices, n_neurons_1]))
bias_hidden_1 = tf.Variable(bias_initializer([n_neurons_1]))
W_hidden_2 = tf.Variable(weight_initializer([n_neurons_1, n_neurons_2]))
bias_hidden_2 = tf.Variable(bias_initializer([n_neurons_2]))
W_hidden_3 = tf.Variable(weight_initializer([n_neurons_2, n_neurons_3]))
bias_hidden_3 = tf.Variable(bias_initializer([n_neurons_3]))
W_hidden_4 = tf.Variable(weight_initializer([n_neurons_3, n_neurons_4]))
bias_hidden_4 = tf.Variable(bias_initializer([n_neurons_4]))


# 2.  inicialize output weights and biases

# In[ ]:


W_out = tf.Variable(weight_initializer([n_neurons_4, 1]))
bias_out = tf.Variable(bias_initializer([1]))


# 3. Create our hidden layers

# In[ ]:


hidden_1 = tf.nn.relu(tf.add(tf.matmul(X, W_hidden_1), bias_hidden_1))
hidden_2 = tf.nn.relu(tf.add(tf.matmul(hidden_1, W_hidden_2), bias_hidden_2))
hidden_3 = tf.nn.relu(tf.add(tf.matmul(hidden_2, W_hidden_3), bias_hidden_3))
hidden_4 = tf.nn.relu(tf.add(tf.matmul(hidden_3, W_hidden_4), bias_hidden_4))


# 4. Create the output layer

# In[ ]:


out = tf.transpose(tf.add(tf.matmul(hidden_4, W_out), bias_out))


# 5. Create the cost function, optimazer, and initialize the network

# In[ ]:


# Cost function
mse = tf.reduce_mean(tf.squared_difference(out, Y))

# Optimizer
opt = tf.train.AdamOptimizer().minimize(mse)

# Init
net.run(tf.global_variables_initializer())


# Now we can train our model with our data

# In[ ]:


mse_train = []
mse_test = []

epochs = 100
while True:

    shuffle_indices = np.random.permutation(np.arange(len(y_train)))
    x_train = x_train[shuffle_indices]
    y_train = y_train[shuffle_indices]
    net.run(opt, feed_dict={X: x_train, Y: y_train})
    mse_train.append(net.run(mse, feed_dict={X: x_train, Y: y_train}))
    mse_test.append(net.run(mse, feed_dict={X: x_test, Y: y_test}))
    print('MSE Test: ', mse_test[-1])
    epochs -= 1
    if mse_test[-1] < 0.01 or epochs == 0:
        break


# After training we can predict the values for the missing function data

# In[ ]:


pred = net.run(out, feed_dict={X: data_pred})
print('----test-data-----')
print(net.run(out, feed_dict={X: x_test}))
print('----pred-data-----')
print(pred)
print([translate(item, -1, 1, 8, 20) for item in pred])
net.close()


# ## Plotting the results
#
# Here we can see a plot, with the previous functions, and the
# completed function based on that data
#
# **Result data**
#
# ![Anotaci%C3%B3n%202018-12-17%20110205.jpg](attachment:Anotaci%C3%B3n%202018-12-17%20110205.jpg)
#
# **Result graphic**
#
# ![Anotaci%C3%B3n%202018-12-17%20110559.jpg](attachment:Anotaci%C3%B3n%202018-12-17%20110559.jpg)
#
# ## Conclusions
#
# After we have trained our neural network, and checked the output results
# for the incomplete function, we can clearly see, that the output is strongly
#  influenced by the orignial known values, as this is a small sample, we dont
# have much training data, and the known data differs strongly from the
# prediction data.
#
# If we scale our sample data set, and known functions, with a better sample,
# our predictions will be even more accurate.
#
# As a final thought, the neural network serves it's purpose, it acts as an
# universal function approximator, so we can have values as close to reality
# as we can get.
#
