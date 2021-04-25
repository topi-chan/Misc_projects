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
colours = ['#000099', '#ffff00'] # yellow is missing. blue is not missing
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
df = df_minus_empty_col

df_descr = pd.read_csv('LCDataDictionary.csv')
df_descr[df_descr.columns[:2]].head(n=10)
df_descr.drop(df_descr.columns[2:],axis=1,inplace=True)
df_descr.head()
df_descr.iloc[:1]

for col in df_descr.columns:
    print(col)
loc = []
for element in almost_empty_col:
    loc.append(df_descr.index[df_descr['LoanStatNew']==element].tolist())
for l in loc:
    print(df_descr.loc[l, 'Description'])

df_descr.loc[50, 'Description']
df_descr.loc[52, 'Description']
df_descr.loc[58, 'Description']
df_descr.loc[145, 'Description']
df_descr.loc[146, 'Description']
df_descr.loc[147, 'Description']
df_descr.loc[148, 'Description']
df_descr.loc[149, 'Description']
df_descr.loc[150, 'Description']

for l in loc:
    print(df_descr.loc[l, 'LoanStatNew'])
df['mths_since_last_delinq'].head()

df['mths_since_last_delinq'] = df['mths_since_last_delinq'].replace(to_replace
                                                    = np.nan, value = -99999)
df['mths_since_last_delinq'].head()

df['mths_since_last_record'].head()
df['mths_since_last_record'] = df['mths_since_last_record'].replace(to_replace
                                                    = np.nan, value = -99999)
df['mths_since_last_record'].head()


#df.iloc[:,50].fillna(0, inplace=True)

#df_empty = pd.DataFrame({'A' : []})
