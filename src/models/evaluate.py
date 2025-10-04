import pandas as pd
import sys
import json
import joblib
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np

def evaluate_model(data_dir, model_file, output_metrics, output_predictions):
    """
    Evaluate trained model on test data and save metrics and predictions.
    """
    # Load test data
    X_test = pd.read_csv(f'{data_dir}/X_test_scaled.csv')
    y_test = pd.read_csv(f'{data_dir}/y_test.csv').values.ravel()
    
    # Load trained model
    model = joblib.load(model_file)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # Create metrics dictionary
    metrics = {
        'mse': float(mse),
        'rmse': float(rmse),
        'mae': float(mae),
        'r2': float(r2)
    }
    
    # Save metrics to JSON
    with open(output_metrics, 'w') as f:
        json.dump(metrics, f, indent=4)
    
    # Save predictions to CSV
    predictions_df = pd.DataFrame({
        'actual': y_test,
        'predicted': y_pred
    })
    predictions_df.to_csv(output_predictions, index=False)
    
    print(f"Model evaluation completed:")
    print(f"  MSE: {mse:.4f}")
    print(f"  RMSE: {rmse:.4f}")
    print(f"  MAE: {mae:.4f}")
    print(f"  R2 Score: {r2:.4f}")
    print(f"\nMetrics saved to: {output_metrics}")
    print(f"Predictions saved to: {output_predictions}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python evaluate.py <data_dir> <model_file> <output_metrics> <output_predictions>")
        sys.exit(1)
    
    data_dir = sys.argv[1]
    model_file = sys.argv[2]
    output_metrics = sys.argv[3]
    output_predictions = sys.argv[4]
    evaluate_model(data_dir, model_file, output_metrics, output_predictions)