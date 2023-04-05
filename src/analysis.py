from sklearn.metrics import mean_absolute_error


def compute_performance(Y_train, Y_train_predict, Y_test, Y_test_predict):
    """Computes the MAE of the given train and test datasets

    Parameters
    -----------
    Y_train : array 
        The results that were used in the train
    Y__train_predict : array 
        The results that were predicted by the train
    Y_test : array 
        The results that were used in the test
    Y_test_predict : array
        The results that were predicted by the test    
    
    Returns
    -----------
    tuple 
        mae_train, mae_test 
        compute the mean absilute error in the train and test between the exact results and what was predicted
    """

    # performance estimation
    mae_train = mean_absolute_error(Y_train, Y_train_predict)
    mae_test = mean_absolute_error(Y_test, Y_test_predict)
    return mae_train, mae_test
