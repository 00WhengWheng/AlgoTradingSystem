class ModelEnsemble:
    def __init__(self, models):
        self.models = models  # Dictionary of model_name: model_instance

    def predict(self, X):
        predictions = {name: model.predict(X) for name, model in self.models.items()}
        # Combine predictions (average, weighted, or voting)
        combined_prediction = sum(predictions.values()) / len(predictions)
        return combined_prediction
