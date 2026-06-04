import pandas as pd

df = pd.read_csv("../data/startup_data.csv")

print(df.head())
print(df.info())
print(df.describe())
