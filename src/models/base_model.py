# models/base_model.py

class BaseModel:
    def __init__(self, data, params):
        """
        Base class for all models.

        Parameters:
        - data (pd.DataFrame): Data to be used by the model.
        - params (dict): Model-specific parameters.
        """
        self.data = data
        self.params = params

    def train(self, X_train, y_train):
        """
        Train the model on training data.
        """
        raise NotImplementedError("Each model must implement the train method.")

    def predict(self, X):
        """
        Make predictions on the given data.
        """
        raise NotImplementedError("Each model must implement the predict method.")
