import pandas as pd
import sys
import json
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score

def grid_search_best_params(data_dir, output_file):
    """
    Perform GridSearch to find best parameters for RandomForestRegressor.
    """
    # Load normalized training data
    X_train = pd.read_csv(f'{data_dir}/X_train_scaled.csv')
    y_train = pd.read_csv(f'{data_dir}/y_train.csv').values.ravel()
    
    # Define parameter grid
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }
    
    # Initialize model
    rf = RandomForestRegressor(random_state=42, n_jobs=-1)
    
    # Perform GridSearch with cross-validation
    print("Starting GridSearch... This may take a while.")
    grid_search = GridSearchCV(
        estimator=rf,
        param_grid=param_grid,
        cv=5,
        scoring='r2',
        n_jobs=-1,
        verbose=1
    )
    
    grid_search.fit(X_train, y_train)
    
    # Get best parameters
    best_params = grid_search.best_params_
    best_score = grid_search.best_score_
    
    # Save best parameters to file
    with open(output_file, 'w') as f:
        json.dump(best_params, f, indent=4)
    
    print(f"\nGridSearch completed:")
    print(f"  Best parameters: {best_params}")
    print(f"  Best CV R2 score: {best_score:.4f}")
    print(f"  Parameters saved to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grid_search.py <data_dir> <output_params_file>")
        sys.exit(1)
    
    data_dir = sys.argv[1]
    output_file = sys.argv[2]
    grid_search_best_params(data_dir, output_file)