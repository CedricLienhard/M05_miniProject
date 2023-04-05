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
    "boston_dataset": ["data/BostonHousing/housing.data"],
    "wine_white_dataset": ["data/WineQuality/winequality-white.csv"],
    "wine_red_dataset": ["data/WineQuality/winequality-red.csv"],
    "all_datasets" : ["data/BostonHousing/housing.data", "data/WineQuality/winequality-white.csv", "data/WineQuality/winequality-red.csv"]
}

protocols = {
    "protocol1": ["proto1"],
    "protocol2": ["proto2"],
    "protocol3": ["proto3"],
    "all_protocols": ["proto1", "proto2", "proto3"]
}

preprocessing_methods = {
    "min_max_scaler": ["min_max"],
    "standard_scaler": ["standard"],
    "polynomial_features": ["polynomial"],
    "all_preprocessings": ["min_max", "standard", "polynomial"]
}

ml_models = {
    "linear_regression": ["linear_regression"],
    "regression_trees": ["regression_tree"],
    "all_models": ["linear_regression", "regression_tree"]
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
    parser.add_argument("--dataset", choices=list(datasets.keys()), default="all_datasets", help='Name of the dataset to use')
    parser.add_argument("--protocol", choices=list(protocols.keys()), default="all_protocols", help='Name of the protocol to use')
    parser.add_argument("--preprocessing", choices=list(preprocessing_methods.keys()), default="all_preprocessings", help='Name of the preprocessing algorithm to use')
    parser.add_argument("--ml_model", choices=list(ml_models.keys()), default="all_models", help='Name of the machine learning algorithm to use')

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

    for dataset in dataset_config:
        print("In dataset: ", dataset)
        print("===============================================================================================")
        for protocol in protocol_config:
            print("  For protocol: ", protocol)
            print("  ---------------------------------------------------------------------------------------------")
            X_train, X_test, Y_train, Y_test = database.get(dataset, protocol)

            for preprocessing in preprocessing_config:
                print("    With preprocessing: ", preprocessing)
                print("    -------------------------------------------------------------------------------------------")
                X_train_norm = preprocessor.apply_selected_preprocessing(
                    preprocessing, X_train
                )
                X_test_norm = preprocessor.apply_selected_preprocessing(
                    preprocessing, X_test
                )

                for algo in ml_config:
                    print("      Using method: ", algo)
                    print("      -----------------------------------------------------------------------------------------")
                    trained_model = algorithm.train_model(
                        algo, X_train_norm, Y_train
                    )
                    Y_train_predict = algorithm.predict(X_train_norm, trained_model)
                    Y_test_predict = algorithm.predict(X_test_norm, trained_model)
                    mae_train, mae_test = analysis.compute_performance(
                        Y_train, Y_train_predict, Y_test, Y_test_predict
                    )
                    print("        Training/ Testing set Mean Absolute Error:", mae_train, "/", mae_test)
                    print("        ---------------------------------------------------------------------------------------")

    
if __name__ == '__main__':
    main()
