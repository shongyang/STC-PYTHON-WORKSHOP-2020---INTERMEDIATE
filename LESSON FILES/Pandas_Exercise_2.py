import pandas as pd

import numpy as np

df1 = pd.read_csv("breakfasts.csv")

print(df1.shape)
print(df1)
df1.drop(["0", "index no"], inplace=True, axis=1)
df1.loc[2] = "an odd fruit", "10 ounces"

df1["ounces"] = df1["ounces"].str.replace(" ounces", "")
df1["ounces"] = df1["ounces"].astype(int)

df1["check"] = df1["ounces"].apply(
    lambda x: "YOU'RE EATING TOO MUCH!!!" if x > 10 else np.nan
)

print(df1)
df1.to_csv("breakfasts_edited_2.csv")