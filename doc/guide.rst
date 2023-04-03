============
 User Guide
============

General Use
------------

This guide explains how to use this package and obtain the same results as shown in the :ref:`results` section.

The main function can be called with different arguments, that can be shown by typing :

.. code-block:: sh

   (project) $ python -m src.main.py --help 

Which should output the following :

.. code-block:: sh
	
   usage: main.py [-h] [--dataset {boston_dataset,wine_dataset}] [--protocol {protocol1,protocol2,protocol3}] [--preprocessing {min_max_scaler,standard_scaler,polynomial_features}]
               [--ml_model {linear_regression,regression_trees}]

   options:
      -h, --help        show this help message and exit
      --dataset {boston_dataset,wine_dataset}
                        Name of the dataset to use
      --protocol {protocol1,protocol2,protocol3}
                        Name of the protocol to use
      --preprocessing {min_max_scaler,standard_scaler,polynomial_features}
                        Name of the preprocessing algorithm to use
      --ml_model {linear_regression,regression_trees}
                        Name of the machine learning algorithm to use

As shown in the help message, the main.py function can be called with different arguments, which are :

- Dataset -> choice between 2 datasets
- Protocol -> choice between 3 protocols 
- Preprocessing -> choice between 3 preprocessing algorithms
- Machine learning algorithm -> choice between 2 machine learning algorithms

These different choices are described here.

It's also possible to call the main.py function without any arguments. In this case, the default arguments are used. 

.. code-block:: sh

   (project) $ python -m src.main.py

The default arguments are : 

- boston_dataset
- protocol1
- min_max_scaler
- linear_regression


Arguments Description
----------------------
Below is a description of the possible arguments to use when calling the main.py function.

Dataset
========
There are 2 choices of datasets:

- Boston Housing Dataset -> you can download the dataset here : https://archive.ics.uci.edu/ml/machine-learning-databases/housing/
- Wine Quality Dataset -> you can download the dataset here : https://archive.ics.uci.edu/ml/datasets/wine+quality 

Protocol
=========
The protocols are defined in the database.py function and define the percentage of data that is used for training and for testing, respetively.

Preprocessing Algorithms 
========================
There are 3 choices of preprocessing algorithms:

- min max scaling -> more details here : https://scikit-learn.org/stable/modules/preprocessing.html
- standard scaling -> more details here : https://scikit-learn.org/stable/modules/preprocessing.html#standardization-or-mean-removal-and-variance-scaling
- min-max and z-normalisation scaling from a configurable set of polynomial features -> more details here : https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html

Machine Learning Algorithm 
===========================
There are 2 choices of ML algorithms:

- Linear Regression -> more details here : https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
- Regression Trees -> more details here : https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html


