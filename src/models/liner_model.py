import numpy as np

import numpy as np
np.seterr(all='warn')

class LinearRegression:
    def __init__(self, l_rate : float or int = 0.001, n_iter : int = 1000):
        self.l_rate = l_rate
        self.n_iter = n_iter
        self.weights = None
        self.bias = None

    def fit(self, X : list or np.array , y : list or np.array):
        if type(X) == list:
            X = np.array(X)
        if type(y) == list:
            y = np.array(y)
        if len(X) != len(y):
            raise ValueError("X and y must have the same length")
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iter):
            y_predicted = np.dot(X, self.weights) + self.bias
            d_w = (1/n_samples) * np.dot(X.T, (y_predicted - y))
            d_b = (1/n_samples) * np.sum(y_predicted-y)
            # print(self.weights)

            self.weights = self.weights - (self.l_rate * d_w)
            self.bias  = self.bias -(self.l_rate * d_b)
        # print(y_predicted.shape)
        return f'LinearRegression Learning Rate = {self.l_rate} n_samples = {n_samples} n_iter = {self.n_iter} feature shape = {self.weights.shape}'

    def predict(self, X_test : list or np.array):
        if type(X_test) == list:
            X_test = np.array(X_test)
        y_test_predicted = np.dot(X_test, self.weights) + self.bias
        return y_test_predicted

    def get_coeff(self):
        return self.weights

    def intercept_(self):
        return self.bias

   

class Perceptron:
    
    def __init__(self, activation_function_name : str = 'linear'):
        self.weights = None
        self.activation_function_name = activation_function_name
        pass 

    def loss(self,y , y_pred):
        return y-y_pred
    
    def activation_function(self, value : int or float):
        if self.activation_function_name == 'linear':
            return value
        if self.activation_function_name == 'sigmoid':
            return 1/(1 + np.exp(-value))


    def fit(self, X : list or np.array = None, y : list or np.array = None , epochs : int = 100, lr : int or float = 0.01 , verbose = False):
        
        if type(X) == list:
            X, y = np.array(X), np.array(y)
        print(X.shape,y.shape)
        self.weights = np.zeros(X.shape)
        # training weights 
        #  d(E)/d(w) = (y - (W.x + b)).X
        for epoch in range(epochs):
            loss = np.mean(self.loss(y, self.activation_function(np.dot(self.weights.T,X))))
            # print(loss)
            self.weights += lr *np.dot(loss,X)

            if verbose:
                print(f"Epoch {epoch+1}/{epochs} :loss =  {loss}")
        return 'Model trained'
    
    def predict(self, X : list or np.array = None):
        if self.weights is None:
            raise ValueError("Model not trained yet")

        return np.dot(self.weights,X)
    
class Metrics:
    
    def __init__(self):
        pass
    
    def mean_squared_error(self,y_true, y_pred):
        return np.mean((y_true - y_pred)**2)
    
    def r2_score(self,y_true, y_pred):
        corr_matrix = np.corrcoef(y_true, y_pred)
        corr = corr_matrix[0, 1]
        return corr ** 2
    
    def rmse(self,y_true, y_pred):
        return np.sqrt(np.mean((y_true- y_pred)**2))
    

# if __name__ == '__main__':