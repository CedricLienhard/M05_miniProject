# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:44:51 2023

@author: Cedric
"""
import numpy as np

import pandas as pd

import os

from sklearn.model_selection import train_test_split

import pkg_resources
DATAFILE = pkg_resources.resource_filename(__name__, "")


#import preprocessor

PROTOCOLS = {
    "proto1": {"train": 0.5, "test": 0.5},
    "proto2": {"train": 0.7, "test": 0.3},
    "proto3": {"train": 0.9, "test": 0.1},
}

VARIABLES_BH = [
    "CRIM",
    "ZN",
    "INDUS",
    "CHAS",
    "NOX",
    "RM",
    "AGE",
    "DIS",
    "RAD",
    "TAX",
    "PTRATIO",
    "B",
    "LSTAT",
    "MEDV",
]

VARIABLES_WQ = [
    "fixed acidity",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "chlorides",
    "free sulfur dioxide",
    "total sulfur dioxide",
    "density"
    "pH",
    "sulphates",
    "alcohol",
    "quality",
]

def load_data(dataset_config):
    """
    Loads the data according to the given configuration

    Parameters
    -----------
    dataset_config : str
        define which dataset to load between the Boston housing or the Wine quality, red or white
                
    Returns
    -----------
    tuple 
        X, Y 
        X is the datas without the results column 
        Y is the results column of the datas (ex: Price, quality)

    """

    # Get the absolute path of the script
    script_path = os.path.abspath(__file__)

    # Get the directory containing the script
    script_dir = os.path.dirname(script_path)
    
    #print(script_dir)
   # print(DATAFILE)

    # Get the path of the dataset
    #file_path = os.path.join(script_dir, dataset_config)
  #  file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), dataset_config)
    print(DATAFILE)
    file_path = os.path.join(DATAFILE, dataset_config)
    print(file_path)

    if dataset_config == 'data/BostonHousing/housing.data':
        #DATAFILE = pkg_resources.resource_filename(__name__, "data/BostonHousing/housing.data")
        
        #with open(file_path, "rt") as f:
        with open(file_path, "rt") as f:
            lines = f.readlines()
            data = []
            for line in lines:
                fields = line.split()
                data.append([float(x) for x in fields])
            data = np.array(data)
            dataset = {}
            j = 0
            for i in VARIABLES_BH:
                dataset[i] = data[:, j]
                j += 1
            X = pd.DataFrame(data[:, :-1], columns=VARIABLES_BH[:-1])
            Y = Y = dataset[VARIABLES_BH[-1]]
    else:
        #DATAFILE = pkg_resources.resource_filename(__name__, "data/WineQuality/housing.data")
        data = pd.read_csv(file_path, header=None)
        data = data[0].str.split(';', expand=True)
        data.columns = data.iloc[0]
        data = data[1:]
        X = data.drop(['"quality"'], axis = 1)    
        Y = data['"quality"']
    return X, Y


def get(dataset_config, protocol_config):
    """
    Split the data for the dataset, according to the given protocol

    Parameters
    ----------
    dataset_config : str
        define which dataset to load (ex: boston_dataset)
    protocol_config : str
        define which protocol to apply (ex: protocol1 -> 50% / 50% )
                
    Returns
    ----------
    tuple 
        X_train, X_test, Y_train, Y_test 
        The value due to the repartitions in the train and the test 

    """
    X, Y = load_data(dataset_config)
    
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=PROTOCOLS[protocol_config]["test"],
        train_size=PROTOCOLS[protocol_config]["train"],
        random_state=5,
    )
    return X_train, X_test, Y_train, Y_test
