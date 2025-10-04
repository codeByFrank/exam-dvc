import pandas as pd
import sys
import json
import joblib
from sklearn.ensemble import RandomForestRegressor

def train_model(data_dir, params_file, output_model):
    """
    Train RandomForestRegressor using best parameters from GridSearch.
    """
    # Load normalized training data
    X_train = pd.read_csv(f'{data_dir}/X_train_scaled.csv')
    y_train = pd.read_csv(f'{data_dir}/y_train.csv').values.ravel()
    
    # Load best parameters
    with open(params_file, 'r') as f:
        best_params = json.load(f)
    
    print("Training model with parameters:")
    for param, value in best_params.items():
        print(f"  {param}: {value}")
    
    # Initialize and train model
    model = RandomForestRegressor(**best_params, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    
    # Save trained model
    joblib.dump(model, output_model)
    
    print(f"\nModel training completed:")
    print(f"  Model saved to: {output_model}")
    print(f"  Training samples: {len(X_train)}")
    print(f"  Features used: {len(X_train.columns)}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python train.py <data_dir> <params_file> <output_model>")
        sys.exit(1)
    
    data_dir = sys.argv[1]
    params_file = sys.argv[2]
    output_model = sys.argv[3]
    train_model(data_dir, params_file, output_model)