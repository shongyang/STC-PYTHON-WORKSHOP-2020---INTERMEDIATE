import pandas as pd
import numpy as np

df1 = pd.read_csv("breakfasts.csv")
print(df1.shape)
print(df1)
df1.drop(["0", "index no"], inplace=True, axis=1)
df1.loc[2] = "an odd fruit", "10 ounces"

print(df1)
df1.to_csv("breakfasts_edited.csv")
