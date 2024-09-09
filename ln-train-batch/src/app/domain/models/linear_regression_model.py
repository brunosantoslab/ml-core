from sklearn.linear_model import LinearRegression
import numpy as np

class LinearRegressionModel:
    """
    Domain model that represents the linear regression model.
    Responsible for training.
    """

    def __init__(self):
        self.model = None

    def train(self, X: np.ndarray, y: np.ndarray):
        """
        Trains the model using the provided features and target values.
        
        Args:
            X (np.ndarray): Feature matrix.
            y (np.ndarray): Target vector.
        """
        self.model = LinearRegression()
        self.model.fit(X, y)
