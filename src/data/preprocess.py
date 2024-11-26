class DataPreprocessor:
    def preprocess(self, data):
        """Clean and preprocess the data."""
        try:
            data.dropna(inplace=True)
            data.reset_index(drop=True, inplace=True)
            return data
        except Exception as e:
            print(f"Error in preprocessing: {e}")
            return None
