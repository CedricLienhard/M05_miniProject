from . import analysis
from . import algorithm
from . import preprocessor
from . import database
import numpy as np
import pandas as pd
from sklearn.datasets import make_regression


def test_MAE():
    Y_train = np.array([1, 2, 3])
    Y_train_predict = np.array([1.5, 2.5, 3.5])
    Y_test = np.array([4, 5, 6])
    Y_test_predict = np.array([4.5, 5.5, 6.5])

    mae_train, mae_test = analysis.compute_performance(
        Y_train, Y_train_predict, Y_test, Y_test_predict
    )
    assert mae_train == 0.5
    assert mae_test == 0.5

def test_train_model():
    # Generate some random data for testing
    X, y = make_regression(n_samples=100, n_features=5, random_state=42)
    X_df = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(5)])
    y_array = np.array(y)

    # Train_the models
    trained_LR_model = algorithm.train_model("linear_regression", X_df, y_array)
    trained_RT_model = algorithm.train_model("regression_tree", X_df, y_array)

    assert trained_LR_model is not None
    assert trained_RT_model is not None



def test_predict():
    # Create some sample data
    X_train = np.array([[1, 2], [3, 4], [5, 6]])
    Y_train = np.array([1, 2, 3])
    X_test = np.array([[7, 8], [9, 10]])

    # Train the model
    trained_model = algorithm.train_model("linear_regression",X_train, Y_train)
    Y_train_predict = algorithm.predict(X_train, trained_model)
    Y_test_predict = algorithm.predict(X_test, trained_model)

    # Check that the output has the correct shape
    assert Y_train_predict.shape == (3,)
    assert Y_test_predict.shape == (2,)


def test_normalize_minMaxScaler():
    # Test that min-max scaling works correctly
    data = np.array([[1, 2], [3, 4]])
    expected_output = np.array([[0, 0], [1, 1]])
    assert np.allclose(preprocessor.normalize_minMaxScaler(data), expected_output)


def test_normalize_standardScaler():
    # Test that standard scaling works correctly
    data = np.array([[1, 2], [3, 4]])
    expected_output = np.array([[-1.0, -1.0], [1.0, 1.0]])
    assert np.allclose(preprocessor.normalize_standardScaler(data), expected_output)


def test_normalize_polynomialFeatures():
    # Test that polynomial feature generation works correctly
    data = np.array([[1, 2], [3, 4]])
    expected_output = np.array([[1, 1, 2, 1, 2, 4], [1, 3, 4, 9, 12, 16]])
    assert np.allclose(
        preprocessor.normalize_polynomialFeatures(data, 2), expected_output
    )

def test_load_data():
    # Test cases for load_data function
    BH_dataset, BH_expected_shape = "data/BostonHousing/housing.data", (506, 13)
    WQR_dataset, WQR_expected_shape = "data/WineQuality/winequality-red.csv", (1599, 11)
    WQW_dataset, WQW_expected_shape = "data/WineQuality/winequality-white.csv", (4898, 11)

    X_BH, Y_BH = database.load_data(BH_dataset)
    X_WQR, Y_WQR = database.load_data(WQR_dataset)
    X_WQW, Y_WQW = database.load_data(WQW_dataset)

    assert X_BH.shape == BH_expected_shape
    assert X_WQR.shape == WQR_expected_shape
    assert X_WQW.shape == WQW_expected_shape


test_MAE()
test_train_model()
test_predict()
test_normalize_standardScaler()
test_normalize_minMaxScaler()
test_normalize_polynomialFeatures()
test_load_data()
