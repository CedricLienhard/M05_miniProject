# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 11:36:37 2023

@author: Cedric
"""


from sklearn.linear_model import LinearRegression


def train_model(X_train, Y_train):
    """
    Optimizes the machine parameters to fit the input data
    
    
    Parameters
    ==========
    X_train :   numpy.ndarray
                The input data matrix. This must be an array with 3 dimensions or
                an iterable containing 2 arrays with 2 dimensions each.  Each
                correspond to the data for one of the two classes, every row
                corresponds to one example of the data set, every column, one
                different feature.
    Returns
    =======
    machine : Machine
        A trained machine.
    """


	# LR model
    lin_model = LinearRegression()
    trained_model = lin_model.fit(X_train, Y_train)
    return trained_model

def predict(X, trained_model):
    
    Y = trained_model.predict(X)
    return Y
	
