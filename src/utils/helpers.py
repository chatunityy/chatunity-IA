def log_message(message):
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def load_data(file_path):
    """Loads data from the specified file path."""
    import pandas as pd
    return pd.read_csv(file_path)

def save_model(model, file_path):
    """Saves the trained model to the specified file path."""
    import joblib
    joblib.dump(model, file_path)

def load_model(file_path):
    """Loads a model from the specified file path."""
    import joblib
    return joblib.load(file_path)

def evaluate_model(model, test_data):
    """Evaluates the model on the provided test data."""
    predictions = model.predict(test_data)
    return predictions