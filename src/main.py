# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:50:40 2023

@author: Cedric
"""

import argparse
import configparser


from . import database
from . import preprocessor
from . import algorithm
from . import analysis


def get_info_from_user():
    """
    Get input from user using argparse

    Parameters
    ==========
    None

    Returns
    =======
    To be filled !

    """
    # Define the configuration options
    config = configparser.ConfigParser()
    config.read("config.ini")
	
    datasets = config["datasets"].keys()
    protocols = config["protocols"].keys()
    preprocessing_methods = config["preprocessing_methods"].keys()
    ml_models = config["ml_models"].keys()

    # Define the command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", choices=datasets, default="boston_dataset", help='Name of the dataset to use')
    parser.add_argument("--protocol", choices=protocols, default="protocol1", help='Name of the protocol to use')
    parser.add_argument("--preprocessing", choices=preprocessing_methods, default="min_max_scaler", help='Name of the preprocessing algorithm to use')
    parser.add_argument("--ml_model", choices=ml_models, default="linear_regression", help='Name of the machine learning algorithm to use')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Load the configuration files
    dataset_config = config["datasets"][args.dataset]
    protocol_config = config["protocols"][args.protocol]
    preprocessing_config = config["preprocessing_methods"][args.preprocessing]
    ml_config = config["ml_models"][args.ml_model]

    return dataset_config, protocol_config, preprocessing_config, ml_config


def main():
	"""Main function to be called from the command-line"""

    (
        dataset_config,
        protocol_config,
        preprocessing_config,
        ml_config,
    ) = get_info_from_user()
    
    X_train, X_test, Y_train, Y_test = database.get(dataset_config, protocol_config)
    
    X_train_norm = preprocessor.apply_selected_preprocessing(
        preprocessing_config, X_train
    )
    
    X_test_norm = preprocessor.apply_selected_preprocessing(
        preprocessing_config, X_test
    )
    
    trained_model = algorithm.train_model(
        ml_config, X_train_norm, Y_train
    )
    

    Y_train_predict = algorithm.predict(X_train_norm, trained_model)
    Y_test_predict = algorithm.predict(X_test_norm, trained_model)
    
    mae_train, mae_test = analysis.compute_performance(
        Y_train, Y_train_predict, Y_test, Y_test_predict
    )
