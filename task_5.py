import helperFunction
from helperTask5 import getXY
import numpy as np
from matplotlib import pyplot as plt

def sigmoid(z):
    return 1/(1+np.exp(-z))

def score(X, weight, bias):
    temp = np.dot(weight.T,X)
    temp = temp+bias
    return sigmoid(temp)

def log_likelihood(y_est,y):
    likelihood = -y*np.log(y_est)-(1-y)*np.log(1-y_est)
    return likelihood

def gradient(Y, Y_est, X, weight):
    temp = (Y_est-Y)*X + weight
    temp_b = (Y_est-Y)
    #temp = temp[np.isnan(temp)==False]
    #temp = np.reshape(3, temp.shape[0]/3)
    #print(temp.shape)
    return (np.mean(temp, axis=1, keepdims=True),
            np.mean(temp_b, axis=1, keepdims=True))

def updateParameter(learning_rate, Y, Y_est, X, weight, bias):
    deriv_w, deriv_b = gradient(Y, Y_est, X, weight)
    return weight-deriv_w*learning_rate, bias-deriv_b*learning_rate

def predict(x, weight, bias):
    score_pred = score(x, weight, bias)
    score_pred = score_pred[np.isnan(score_pred)==False]
    return score_pred>=0.5

def wrong_pred(y_pred, Y):
    return np.sum(y_pred!=Y)

data = helperFunction.readFile()
X,Y = getXY(data)
learning_rate = .01
num_iteration = 2

n_samples = X.shape[0]

n_train = int(n_samples*0.70)
n_validation = int(n_samples*0.15)

#not shuffling data, already in random order
X_train = np.float32(X[0:n_train,:].T)
X_validation = np.float32(X[n_train:n_train+n_validation,:].T)
X_test = np.float32(X[n_train+n_validation:, :].T)

Y_train = np.float32(Y[0:n_train])
Y_validation = np.float32(Y[n_train:n_train+n_validation])
Y_test = np.float32(Y[n_train+n_validation:])


weight = np.random.rand(X_train.shape[0],1)/np.sqrt(X_train.shape[1])
bias = np.zeros((1,))
for i in range(num_iteration):
    y_est = score(X_train, weight, bias)
    #check for nan
    #y_est[np.isnan(y_est)==True]
    l = log_likelihood(y_est, Y_train)
    deriv = gradient(Y_train, y_est, X_train, weight)
    #weight, bias = updateParameter(learning_rate, Y_train, y_est, X_train, weight, bias)

y_pred = predict(X_test, weight, bias)
