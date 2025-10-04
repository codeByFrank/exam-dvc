import pandas as pd
import sys
import os
from sklearn.model_selection import train_test_split

def split_data(input_path, output_dir):
    """
    Split data into training and testing sets.
    Target variable: silica_concentrate (last column)
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Load data
    print(f"Loading data from: {input_path}")
    df = pd.read_csv(input_path)
    
    print(f"Data loaded. Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    
    # Check if target column exists
    if 'silica_concentrate' not in df.columns:
        print(f"ERROR: 'silica_concentrate' column not found!")
        print(f"Available columns: {df.columns.tolist()}")
        sys.exit(1)
    
    # Drop non-numeric columns (like date)
    columns_to_drop = ['silica_concentrate']
    if 'date' in df.columns:
        columns_to_drop.append('date')
        print("Dropping 'date' column (non-numeric)")
    
    # Separate features and target
    X = df.drop(columns_to_drop, axis=1)
    y = df['silica_concentrate']
    
    print(f"Features used: {X.columns.tolist()}")
    
    # Split data: 80% train, 20% test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Save datasets
    print(f"Saving datasets to: {output_dir}")
    X_train.to_csv(f'{output_dir}/X_train.csv', index=False)
    X_test.to_csv(f'{output_dir}/X_test.csv', index=False)
    y_train.to_csv(f'{output_dir}/y_train.csv', index=False)
    y_test.to_csv(f'{output_dir}/y_test.csv', index=False)
    
    print(f"Data split completed:")
    print(f"  Training samples: {len(X_train)}")
    print(f"  Testing samples: {len(X_test)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python data_split.py <input_csv> <output_dir>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_dir = sys.argv[2]
    
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"ERROR: Input file not found: {input_path}")
        sys.exit(1)
    
    split_data(input_path, output_dir)