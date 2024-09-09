import pandas as pd

class Dataset:
    """
    Value object representing a dataset containing features and target values.
    Used for training and predictions.
    """
    def __init__(self, features: pd.DataFrame, target: pd.Series):
        self.features = features
        self.target = target