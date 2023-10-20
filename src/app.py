import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import KNNImputer
import statsmodels.api as sm

dataset = pd.read_csv("https://raw.githubusercontent.com/4GeeksAcademy/data-preprocessing-project-tutorial/main/AB_NYC_2019.csv")
df = pd.DataFrame(dataset)

print(df.info())
count_unique = df.nunique()
df.describe()

y = df.price.values
print(y)
plt.hist(y, bins=20)
plt.show
