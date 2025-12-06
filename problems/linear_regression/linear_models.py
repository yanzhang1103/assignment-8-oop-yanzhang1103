import numpy as np

class LinearRegressionClosedForm:
    def __init__(self):
        self.weights = None

    def fit(self, X, y):
        X_bias = np.c_[np.ones(X.shape[0]), X]
        self.weights = np.linalg.pinv(X_bias.T @ X_bias) @ X_bias.T @ y

    def predict(self, X):
        if self.weights is None:
            raise ValueError("Model not trained yet.")
        X_bias = np.c_[np.ones(X.shape[0]), X]
        return X_bias @ self.weights

