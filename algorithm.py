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
    To be filled !
                
    Returns
    =======
    To be filled !

    """

    # LR model
    lin_model = LinearRegression()
    trained_model = lin_model.fit(X_train, Y_train)
    return trained_model


def predict(X, trained_model):
    """
    Best fit for the input data according to the trained model

    Parameters
    ==========
    To be filled !
                
    Returns
    =======
    To be filled !

    """

    Y = trained_model.predict(X)
    return Y
