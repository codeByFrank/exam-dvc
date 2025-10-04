import pandas as pd
import sys
from sklearn.preprocessing import StandardScaler
import joblib

def normalize_data(input_dir, output_dir):
    """
    Normalize training and testing data using StandardScaler.
    Fit scaler on training data only.
    """
    # Load data
    X_train = pd.read_csv(f'{input_dir}/X_train.csv')
    X_test = pd.read_csv(f'{input_dir}/X_test.csv')
    
    # Initialize and fit scaler on training data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Convert back to DataFrames
    X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
    X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)
    
    # Save normalized data
    X_train_scaled.to_csv(f'{output_dir}/X_train_scaled.csv', index=False)
    X_test_scaled.to_csv(f'{output_dir}/X_test_scaled.csv', index=False)
    
    # Save scaler for later use
    joblib.dump(scaler, f'{output_dir}/scaler.pkl')
    
    print(f"Data normalization completed:")
    print(f"  Features normalized: {len(X_train.columns)}")
    print(f"  Scaler saved to: {output_dir}/scaler.pkl")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python normalize.py <input_dir> <output_dir>")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    normalize_data(input_dir, output_dir)