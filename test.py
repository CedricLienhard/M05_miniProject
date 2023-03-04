import analysis
import algorithm
import preprocessor
import numpy as np

def test_MAE():
	Y_train = np.array([1, 2, 3])
	Y_train_predict = np.array([1.5, 2.5, 3.5])
	Y_test = np.array([4, 5, 6])
	Y_test_predict = np.array([4.5, 5.5, 6.5])

	mae_train, mae_test = analysis.compute_performance(Y_train, Y_train_predict, Y_test, Y_test_predict)
	assert mae_train == 0.5
	assert mae_test == 0.5
        
       

test_MAE()

