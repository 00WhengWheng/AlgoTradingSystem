# models/model_trainer.py

import os
import joblib
from sklearn.ensemble import RandomForestClassifier  # Example model, can be replaced
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

class ModelTrainer:
    def __init__(self, model, model_name, save_path='../models/saved_models'):
        """
        Initializes the ModelTrainer.

        Parameters:
        - model: Instantiated model object (e.g., RandomForestClassifier()).
        - model_name (str): Name for the model file.
        - save_path (str): Path to save the trained model.
        """
        self.model = model
        self.model_name = model_name
        self.save_path = save_path
        os.makedirs(self.save_path, exist_ok=True)

    def train(self, X, y):
        """
        Trains the model.
        """
        self.model.fit(X, y)
        print("Model training complete.")

    def save_model(self):
        """
        Saves the trained model to the specified directory.
        """
        model_filepath = os.path.join(self.save_path, f"{self.model_name}.joblib")
        joblib.dump(self.model, model_filepath)
        print(f"Model saved to {model_filepath}")

    def load_model(self):
        """
        Loads a saved model.
        """
        model_filepath = os.path.join(self.save_path, f"{self.model_name}.joblib")
        if os.path.exists(model_filepath):
            self.model = joblib.load(model_filepath)
            print(f"Model loaded from {model_filepath}")
        else:
            print(f"No saved model found at {model_filepath}")

# Example usage
if __name__ == "__main__":
    # Load data and split (using dummy data here for illustration)
    data = pd.read_csv('../data/processed/sample_data.csv')
    X = data.drop(columns=['target'])
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Instantiate and train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    trainer = ModelTrainer(model=model, model_name="random_forest_model")
    trainer.train(X_train, y_train)

    # Save trained model
    trainer.save_model()
