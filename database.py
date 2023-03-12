# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:44:51 2023

@author: Cedric
"""
import numpy as np

import pandas as pd

import csv 

import os

from sklearn.model_selection import train_test_split

PROTOCOLS = {
        'proto1': {'train': 0.5, 'test': 0.5},
        'proto2': {'train': 0.5, 'test': 0.2},
        }

VARIABLES_BH = [
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
VARIABLES_WQ = [
	'FA',   # fixed acidity
	'VA',   # volatile acidity
	'CA',   # citric acid
	'RS',   # residual sugar
	'CHL',  # chlorides
	'FSD',  # free sulfur dioxide
	'TSD',  # total sulfur dioxide
	'DENS', # density
	'PH',   # pH
	'SULP', # sulphates 
	'ALC',  # alcohol
	'QLT'   # quality
        ]

def load_data(dataset_config):
	
	# Get the absolute path of the script
	script_path = os.path.abspath(__file__)

	# Get the directory containing the script
	script_dir = os.path.dirname(script_path)

	# Get the path of the dataset
	file_path = os.path.join(script_dir, dataset_config)
	
	name_datasets = dataset_config['datasets']

	VARIABLES = variables_to_choose(name_datasets)
	
	with open(file_path, 'rt') as f:
		data = []
		
		if name_datasets == 'bostonDataset' : 
                        lines = f.readlines()
                        for line in lines:
                                fields = line.split()
                                data.append([float(x) for x in fields])			
                elif name_datasets == 'winedataSet':
			file_path_red = os.path.join(file_path, 'winequality-red.csv')
			file_path_white = os.path.join(file_path, 'winequality-white.csv')

			data = list(csv.reader(file_path_red, delimiter=';'))
			data.append(list(csv.reader(file_path_white, delimiter=';')))
		
		data = np.array(data)
		dataset = {}
		j = 0
		for i in VARIABLES :
			dataset[i] = data[:, j]
			j += 1   
	return data, dataset
 
def get(datasetPath, protocol):
    raw_data, dataset = load_data(datasetPath)
    VARIABLES = variables_to_choose(datasetPath['datasets'])

    # use all variables except last column, which is the output 
    X = pd.DataFrame(raw_data[:, :-1], columns = VARIABLES[:-1])
    Y = dataset[-1]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = PROTOCOLS[protocol]['test'], train_size = PROTOCOLS[protocol]['train'], random_state=5)
    
    return X_train, X_test, Y_train, Y_test


def variables_to_choose(selected_data_set):
	if selected_data_set == 'wineDataset':
		return VARIABLES_WQ
	else :
		return VARIABLES_BH