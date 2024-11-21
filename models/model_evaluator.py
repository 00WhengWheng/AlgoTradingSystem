# models/model_evaluator.py

import os
import joblib
import json
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

class ModelEvaluator:
    def __init__(self, model_name, eval_save_path='../models/evaluation'):
        """
        Initializes the ModelEvaluator.

        Parameters:
        - model_name (str): Name of the model file.
        - eval_save_path (str): Path to save evaluation metrics.
        """
        self.model_name = model_name
        self.eval_save_path = eval_save_path
        os.makedirs(self.eval_save_path, exist_ok=True)
        self.model = self.load_model()

    def load_model(self):
        """
        Loads a saved model.
        """
        model_filepath = f"../models/saved_models/{self.model_name}.joblib"
        if os.path.exists(model_filepath):
            model = joblib.load(model_filepath)
            print(f"Model loaded from {model_filepath}")
            return model
        else:
            raise FileNotFoundError(f"No saved model found at {model_filepath}")

    def evaluate(self, X_test, y_test):
        """
        Evaluates the model on the test set.
        """
        predictions = self.model.predict(X_test)
        metrics = {
            "accuracy": accuracy_score(y_test, predictions),
            "precision": precision_score(y_test, predictions, average='weighted'),
            "recall": recall_score(y_test, predictions, average='weighted'),
            "f1_score": f1_score(y_test, predictions, average='weighted')
        }
        print("Model evaluation metrics:", metrics)
        return metrics

    def save_evaluation(self, metrics):
        """
        Saves evaluation metrics to a JSON file.
        """
        eval_filepath = os.path.join(self.eval_save_path, f"{self.model_name}_evaluation.json")
        with open(eval_filepath, 'w') as f:
            json.dump(metrics, f, indent=4)
        print(f"Evaluation metrics saved to {eval_filepath}")

# Example usage
if __name__ == "__main__":
    # Load test data
    data = pd.read_csv('../data/processed/sample_data.csv')
    X = data.drop(columns=['target'])
    y = data['target']
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Evaluate model
    evaluator = ModelEvaluator(model_name="random_forest_model")
    metrics = evaluator.evaluate(X_test, y_test)

    # Save evaluation metrics
    evaluator.save_evaluation(metrics)
