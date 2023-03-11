# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:44:51 2023

@author: Cedric
"""
import numpy as np

import pandas as pd

import os

from sklearn.model_selection import train_test_split

PROTOCOLS = {
        'proto1': {'train': 0.5, 'test': 0.5},
        'proto2': {'train': 0.5, 'test': 0.2},
        }

VARIABLES = [
        'CRIM',
        'ZN',
        'INDUS',
        'CHAS',
        'NOX',
        'RM',
        'AGE',
        'DIS',
        'RAD',
        'TAX',
        'PTRATIO',
        'B',
        'LSTAT',
        'MEDV',
        ]

def load_data(dataset_config):
	
	# Get the absolute path of the script
	script_path = os.path.abspath(__file__)

	# Get the directory containing the script
	script_dir = os.path.dirname(script_path)

	# Get the path of the dataset
	file_path = os.path.join(script_dir, dataset_config)
	
	with open(file_path, 'rt') as f:
		lines = f.readlines()
		data = []
		for line in lines:
			fields = line.split()
			data.append([float(x) for x in fields])
		data = np.array(data)
		boston_dataset = {}
		j = 0
		for i in VARIABLES :
			boston_dataset[i] = data[:, j]
			j += 1   
	return data, boston_dataset
 
def get(datasetPath, protocol):
    raw_data, boston_dataset = load_data(datasetPath)
    # use all variables except the price (last column), which is the output 
    X = pd.DataFrame(raw_data[:, :-1], columns = VARIABLES[:-1])
    Y = boston_dataset['MEDV']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = PROTOCOLS[protocol]['test'], train_size = PROTOCOLS[protocol]['train'], random_state=5)
    
    return X_train, X_test, Y_train, Y_test


