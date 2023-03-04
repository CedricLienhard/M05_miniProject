# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 11:36:37 2023

@author: Cedric
"""


from sklearn.linear_model import LinearRegression


def trainMachine(X_train, Y_train, X_test):

	# LR model
	lin_model = LinearRegression()
	lin_model.fit(X_train, Y_train)
    
    	#evaluate on training and testing data
	Y_train_predict = lin_model.predict(X_train)
	Y_test_predict = lin_model.predict(X_test)
	
	return Y_train_predict, Y_test_predict
	
