# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:50:40 2023

@author: Cedric
"""

import argparse
import configparser


#from . import database
import database
import preprocessor
import algorithm
import analysis
#from . import preprocessor
#from . import algorithm
#from . import analysis


datasets = {
    "boston_dataset": "data/BostonHousing/housing.data",
    "wine_white_dataset": "data/WineQuality/winequality-white.csv",
    "wine_red_dataset": "data/WineQuality/winequality-red.csv",
}

protocols = {
    "protocol1": "proto1",
    "protocol2": "proto2",
    "protocol3": "proto3"
}

preprocessing_methods = {
    "min_max_scaler": "1",
    "standard_scaler": "2",
    "polynomial_features": "3"
}

ml_models = {
    "linear_regression": "linear_regression",
    "regression_trees": "regression_trees"
}


def get_info_from_user():
    """Get input from user using argparse

    Returns
    ----------
    tuple
        dataset_config, protocol_config, preprocessing_config, ml_config
        returns the configurations for dataset, protocol, preprocessing and the algorithm to apply
    """

    # Define the command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", choices=list(datasets.keys()), default="boston_dataset", help='Name of the dataset to use')
    parser.add_argument("--protocol", choices=list(protocols.keys()), default="protocol1", help='Name of the protocol to use')
    parser.add_argument("--preprocessing", choices=list(preprocessing_methods.keys()), default="min_max_scaler", help='Name of the preprocessing algorithm to use')
    parser.add_argument("--ml_model", choices=list(ml_models.keys()), default="linear_regression", help='Name of the machine learning algorithm to use')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Load the configuration files
    dataset_config = datasets[args.dataset]
    protocol_config = protocols[args.protocol]
    preprocessing_config = preprocessing_methods[args.preprocessing]
    ml_config = ml_models[args.ml_model]
    
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
    
if __name__ == '__main__':
    main()
