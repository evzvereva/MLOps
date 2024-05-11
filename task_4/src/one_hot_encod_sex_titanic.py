import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("../datasets/titanic.csv", sep=",")

enc = OneHotEncoder(drop='if_binary', sparse_output=False)
sex_enc = enc.fit_transform(df[['Sex']])
df['Sex_enc'] = sex_enc
df.to_csv("../datasets/titanic.csv", index=False)
