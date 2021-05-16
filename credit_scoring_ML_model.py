import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import re

data = pd.read_csv('credit_scoring_for_model_final.csv')

only_num_series = data.select_dtypes(include=np.number).columns.tolist()
all_series = []
for col in data.columns:
    all_series.append(col)
non_num_series = set(only_num_series) ^ set(all_series)
non_num_series
data['loan_status'].head(n=12)

for i, row in data['loan_status'].iteritems():
    if row == "Charged Off":
        row_value = 0.0
    elif row == "Fully Paid":
        row_value = 1.0
    data.at[i, 'loan_status'] = row_value

y = data['loan_status']

x_data = data.drop(columns='loan_status')

x = (x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data)).values

for col in x.columns:
    print(col)

x.drop(axis=1, labels=['Unnamed: 0', 'Unnamed: 0.1'], inplace=True)
list_of_important_cols = x.columns.tolist
print(type(list_of_important_cols))




#####Here prediction analysis begin######

data.corr()
print(len(data.columns))

y = data['loan_status']
y = data['loan_status'].astype(float)

data['loan_status'] = data['loan_status'].astype(float)
data['loan_status'].dtype
x_important_cols = data[['loan_status', 'loan_amnt', 'int_rate', 'zip_code', 'A', 'B', 'C', 'D',
                        § 'E', 'F', 'G']]
x_important_cols.head()

x_important_cols.corr()
#here it's weird, since F and G are more payable than E/D - unregistered income?
data.columns.tolist()
x_2important_cols = []
x_2important_cols = data[['loan_status','A1',
 'A2',
 'A3',
 'A4',
 'A5',
 'B1',
 'B2',
 'B3',
 'B4',
 'B5',
 'C1',
 'C2',
 'C3',
 'C4',
 'C5',
 'D1',
 'D2',
 'D3',
 'D4',
 'D5',
 'E1',
 'E2',
 'E3',
 'E4',
 'E5',
 'F1',
 'F2',
 'F3',
 'F4',
 'F5',
 'G1',
 'G2',
 'G3',
 'G4',
 'G5']]

dd = x_2important_cols.corr()
dd


for col in dd:
    if re.search("A", col):

    print(col)
    print("x")



display(data['loan_status'].dtypes)
x['loan_amnt'].head(n=15)
plt.scatter(x.loan_amnt, y)

sns.heatmap(x.corr(), xticklabels=x.corr().columns, yticklabels=x.corr().columns)

col_mapping_dict = {c[0]:c[1] for c in enumerate(x.columns)}
col_mapping_dict
#use iloc for columns optimization
x.loan_amnt.head(n=15)
plt.scatter(x.loan_amnt, y)
np.corrcoef(x.loan_amnt, y)

tittles = x.iloc[:,103:]
title_corr = tittles.corr()
sns.heatmap(title_corr, xticklabels=title_corr.columns,
            yticklabels=y.columns)

sns.heatmap(corr, xticklabels=x.corr.columns,


                                     yticklabels=x.corr.columns)
#
# df_combined = [x, y]
#
# data.concat()
