# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 20:33:56 2023

@author: Cedric
"""
from sklearn import preprocessing


def normalize_minMaxScaler(data_to_process):
    min_max_scaler = preprocessing.MinMaxScaler()
    processedData = min_max_scaler.fit_transform(data_to_process)

    return processedData


def normalize_standardScaler(data_to_process):
    scaler = preprocessing.StandardScaler().fit(data_to_process)
    processedData = scaler.transform(data_to_process)

    return processedData


def normalize_polynomialFeatures(data_to_process, polyDegree):
    poly = preprocessing.PolynomialFeatures(
        degree=polyDegree, interaction_only=False, include_bias=True
    )
    processedData = poly.fit_transform(data_to_process)

    return processedData


def apply_selected_preprocessing(selected_preprocessing, data_to_process):
    # list of available functions
    preprocessing_choices = [
        normalize_minMaxScaler,
        normalize_standardScaler,
        normalize_polynomialFeatures,
    ]

    if selected_preprocessing == "1":
        processed_data = preprocessing_choices[0](data_to_process)
    elif selected_preprocessing == "2":
        processed_data = preprocessing_choices[1](data_to_process)
    elif selected_preprocessing == "3":
        processed_data = preprocessing_choices[2](data_to_process, 2)
    else:
        print("Invalid preprocessing choice !")

    return processed_data
