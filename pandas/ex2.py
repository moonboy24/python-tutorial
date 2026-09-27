import pandas as pd

df = pd.read_csv("ex2.csv")
print(df)

df.to_csv("ex2o.csv" , index=False)