from sklearn.metrics import mean_absolute_error


def compute_performance(Y_train, Y_train_predict, Y_test, Y_test_predict):
    """
    Computes the MAE of the given train and test datasets

    Parameters
    ==========
    To be filled !
                
    Returns
    =======
    To be filled !

    """

    # performance estimation
    mae_train = mean_absolute_error(Y_train, Y_train_predict)
    mae_test = mean_absolute_error(Y_test, Y_test_predict)
    print("Training set Mean Absolute Error:", mae_train)
    print("Testing set Mean Absolute Error:", mae_test)
    return mae_train, mae_test
