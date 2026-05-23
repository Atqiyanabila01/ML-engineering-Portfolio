import pandas as pd
import os

def load_data(filepath):
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File {filepath} not found")
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def validate_data(df):
    if df is None:
        return False
    if df.empty:
        print("Error: DataFrame is empty")
        return False
    print(f"Data validated: {df.shape[0]} rows, {df.shape[1]} columns")
    return True

# Main execution
df = load_data('titanic_clean.csv')
if validate_data(df):
    print("Processing successful")
else:
    print("Processing failed")