# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 11:36:37 2023

@author: Cedric
"""


from sklearn.linear_model import LinearRegression


def train_model(X_train, Y_train):

	# LR model
	lin_model = LinearRegression()
	trained_model = lin_model.fit(X_train, Y_train)
	return trained_model

def predict(X, trained_model):
    
    Y = trained_model.predict(X)
    return Y
	
