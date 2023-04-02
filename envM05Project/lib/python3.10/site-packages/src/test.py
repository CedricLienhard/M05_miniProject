import analysis
import algorithm
import preprocessor
import numpy as np


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


test_MAE()
test_predict()
test_normalize_standardScaler()
test_normalize_minMaxScaler()
test_normalize_polynomialFeatures()
