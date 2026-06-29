# Jour 4 - Statistiques avec CSV

import pandas as pd

df = pd.read_csv("titanic.csv")

print(df.head())
print(df.describe())
