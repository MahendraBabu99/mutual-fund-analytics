import pandas as pd
import os

folder = "data/raw"

csv_files = [f for f in os.listdir(folder) if f.endswith(".csv")]

for file in csv_files:

    path = os.path.join(folder, file)

    print("=" * 80)
    print("FILE:", file)

    df = pd.read_csv(path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())

    print("=" * 80)