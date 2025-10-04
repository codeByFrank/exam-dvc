import os, argparse, pandas as pd, yaml
from sklearn.preprocessing import StandardScaler, MinMaxScaler
def main(in_dir, out_dir, params_path):
    os.makedirs(out_dir, exist_ok=True)
    prm = yaml.safe_load(open(params_path))
    Xtr = pd.read_csv(f"{in_dir}/X_train.csv")
    Xte = pd.read_csv(f"{in_dir}/X_test.csv")
    scaler = MinMaxScaler() if prm["scale"]["method"]=="minmax" else StandardScaler()
    Xtr_sc = scaler.fit_transform(Xtr); Xte_sc = scaler.transform(Xte)
    pd.DataFrame(Xtr_sc, columns=Xtr.columns).to_csv(f"{out_dir}/X_train_scaled.csv", index=False)
    pd.DataFrame(Xte_sc, columns=Xte.columns).to_csv(f"{out_dir}/X_test_scaled.csv", index=False)
    print("Scaling done.")
if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("-i","--in_dir", default="data/processed_data")
    p.add_argument("-o","--out_dir", default="data/processed_data")
    p.add_argument("-p","--params", default="params.yaml")
    a = p.parse_args(); main(a.in_dir, a.out_dir, a.params)