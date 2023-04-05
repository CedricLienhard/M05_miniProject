# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 20:33:56 2023

@author: Cedric
"""
from sklearn import preprocessing


def normalize_minMaxScaler(data_to_process):
    """min max scaler normalization

    Parameters
    -----------
    data_to_process : DataFrame
        It is the data to process (the X)
                    
    Returns
    -----------
    DataFrame
        processedData
        returns the data processed with the min max scaler normalization 
    """
    min_max_scaler = preprocessing.MinMaxScaler()
    processedData = min_max_scaler.fit_transform(data_to_process)

    return processedData


def normalize_standardScaler(data_to_process):
    """standard scaler normalization

    Parameters
    -----------
    data_to_process : DataFrame
        It is the data to process (the X)
                    
    Returns
    -----------
    DataFrame
        processedData
        returns the data processed with the standard scaler normalization 
    """
    scaler = preprocessing.StandardScaler().fit(data_to_process)
    processedData = scaler.transform(data_to_process)

    return processedData


def normalize_polynomialFeatures(data_to_process, polyDegree):
    """polynomial normalization

    Parameters
    -----------
    data_to_process : DataFrame
        It is the data to process (the X)
    polyDegree : int 
        The degree of the polynomial used in the normalization
                    
    Returns
    -----------
    DataFrame
        processedData
        returns the data processed with the polynomial normalization 
    """
    poly = preprocessing.PolynomialFeatures(
        degree=polyDegree, interaction_only=False, include_bias=True
    )
    processedData = poly.fit_transform(data_to_process)

    return processedData


def apply_selected_preprocessing(selected_preprocessing, data_to_process):
    """apply given preprocessing type on the data

    Parameters
    -----------
    selected_preprocessing : str
        gives which preprocess is selected (min_max, standard or polynomial)
    data_to_process : DataFrame 
        It is the data to process (the X)

    Returns
    -----------
    DataFrame
        processedData
        returns the data processed with the selected normalization 
    """
    # list of available functions
    preprocessing_choices = [
        normalize_minMaxScaler,
        normalize_standardScaler,
        normalize_polynomialFeatures,
    ]

    if selected_preprocessing == "min_max":
        processed_data = preprocessing_choices[0](data_to_process)
    elif selected_preprocessing == "standard":
        processed_data = preprocessing_choices[1](data_to_process)
    elif selected_preprocessing == "polynomial":
        processed_data = preprocessing_choices[2](data_to_process, 2)
    else:
        print("Invalid preprocessing choice !")

    return processed_data
