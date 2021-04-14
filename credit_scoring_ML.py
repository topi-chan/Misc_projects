import pandas as pd
import numpy as np
import matplotlib
import sklearn
import seaborn as sns
import csv


df = pd.read_csv('Loan_data.csv')
empty_col = []
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))
    if pct_missing == 1:
        empty_col.append(col)
print(empty_col)
df.head()


cols = df.columns[:30]
colours = ['#000099', '#ffff00'] # yellow is missing. blue is not missing.
sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colours))
print(empty_col)
df_minus_empty_col = df.drop(empty_col, axis=1)

print(df_minus_empty_col.head(n=20))

almost_empty_col = []
for col in df_minus_empty_col.columns:
    pct_missing = np.mean(df[col].isnull())
    value = float(np.mean(df[col].isnull()))
    print('{} - {}%'.format(col, round(pct_missing*100)))
    if round(pct_missing) == 1:
        almost_empty_col.append(col), almost_empty_col.append(value)
print(almost_empty_col)

with open('LCDataDictionary.csv', newline='') as csvfile:
    read_data_dict = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in read_data_dict:
        print(', '.join(row))

data_dict = pd.read_csv('LCDataDictionary.csv')
print(data_dict.head(n=20))
info_dict = {}
for index, row in data_dict.iterrows():
    if row.any() in almost_empty_col:
        print('x', row)
