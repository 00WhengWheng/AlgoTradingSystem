class BaseModel:
    def train(self, X_train, y_train):
        raise NotImplementedError("Train method must be implemented.")

    def predict(self, X):
        raise NotImplementedError("Predict method must be implemented.")

    def evaluate(self, X_val, y_val):
        raise NotImplementedError("Evaluate method must be implemented.")
