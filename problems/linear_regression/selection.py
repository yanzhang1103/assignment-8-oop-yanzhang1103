import numpy as np

def train_test_split(X, y, test_size=0.2):
    n = len(X)
    indices = np.arange(n)
    np.random.shuffle(indices)

    test_size = int(n * test_size)
    test_idx = indices[:test_size]
    train_idx = indices[test_size:]

    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]


class LinearRegressionGradientDescent:
    def __init__(self, lr=0.01, epochs=1000):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
    
    def fit(self, X, y):
        X_bias = np.c_[np.ones(X.shape[0]), X]
        n_samples, n_features = X_bias.shape

        self.weights = np.zeros(n_features)

        for _ in range(self.epochs):
            y_pred = X_bias @ self.weights
            gradient = (1 / n_samples) * (X_bias.T @ (y_pred - y))
            self.weights -= self.lr * gradient

    def predict(self, X):
        X_bias = np.c_[np.ones(X.shape[0]), X]
        return X_bias @ self.weights
