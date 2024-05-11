import pandas as pd

df = pd.read_csv("titanic.csv", sep=",")

df['Age'] = df['Age'].fillna(df['Age'].mean()).round(1)

df.to_csv("titanic.csv", index=False)
