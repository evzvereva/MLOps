import pandas as pd

df = pd.read_csv("../datasets/titanic.csv", sep=",")

df['Age'] = df['Age'].fillna(df['Age'].mean()).round(1)

df.to_csv("../datasets/titanic.csv", index=False)
