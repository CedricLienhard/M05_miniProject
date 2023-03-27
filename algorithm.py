# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 11:36:37 2023

@author: Cedric
"""


from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

def train_model(model, X_train, Y_train):
    """
    Optimizes the machine parameters to fit the input data

    Parameters
    ==========
    To be filled !
                
    Returns
    =======
    To be filled !

    """
    if model == "linear_regression":
        # LR model
        lin_model = LinearRegression()
        trained_model = lin_model.fit(X_train, Y_train)
    elif model == "regression_trees":
        # RT model
        rt_model = DecisionTreeRegressor(random_state=44, criterion="absolute_error", max_depth=5)
        trained_model = rt_model.fit(X_train, Y_train)
    else :
        print("Algorithm is not implemented !")
        return
    
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
