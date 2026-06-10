import pandas as pd

df = pd.read_csv("maison.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

import matplotlib.pyplot as plt

df["Price"].hist()
plt.show()