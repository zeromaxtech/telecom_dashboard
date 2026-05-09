import pandas as pd

df = pd.read_csv("trai_data.csv")
print(df.head())
print("\nData shape:", df.shape)
print("\nColumns:", df.columns.tolist())
