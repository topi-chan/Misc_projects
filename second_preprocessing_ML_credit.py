import pandas as pd
import numpy as np
import csv
from credit_scoring_ML import print_description
from credit_scoring_ML import check_consistency

data = pd.read_csv('credit_scoring_for_model.csv')

for col in data.columns:
    print(col)

data.applymap(np.isreal)

only_num_series = data.select_dtypes(include=np.number).columns.tolist()
all_series = []
for col in data.columns:
    all_series.append(col)
non_num_series = set(only_num_series) ^ set(all_series)
#still non numeric:
{'earliest_cr_line',
 'int_rate',
 'issue_d',
 'last_credit_pull_d',
 'last_pymnt_d',
 'loan_status',
 'revol_util'}
#int rate is percent, rest is date
non_num_list = [item for item in all_series if item not in only_num_series]
non_num_list
print_description(non_num_list)
data['int_rate'].dtype
data['int_rate'] = data['int_rate'].astype('string')
data['int_rate'].dtype
for i, row in data['int_rate'].iteritems():
    row_value = row.replace('%', '')
    data.at[i, 'int_rate'] = row_value
data['int_rate'] = data['int_rate'].astype('float')
data['int_rate'].mean()
data['int_rate'].median()
data['int_rate'].std()

data['issue_d'].head(n=25)
check_consistency('issue_d', '2011-12-01', '2011-11-01')
#column is consisted and seems sorted - is this data necessary?

data['loan_status']
#!!column to be predicted!

data['earliest_cr_line'].head(n=25)


df_descr = pd.read_csv('LCDataDictionary.csv')


df_descr.loc[18, 'Description']
df_descr.loc[91, 'Description']
data['revol_util'].head(n=25)
#! it's very important factor!/ usage of credit ratio

data['revol_util'] = data['revol_util'].astype('string')
data['revol_util'].dtype
data['revol_util'].isnull().values.any()
data['revol_util'].isna().sum()
data.sum(axis=1)
data.dropna(subset=['revol_util'], inplace=True)
data.sum(axis=1)
#dropped empty, since it's important factor for prediction and empty columns
#number was not substantial

for i, row in data['revol_util'].iteritems():
    row_value = row.replace('%', '')
    data.at[i, 'revol_util'] = row_value
data['revol_util'] = data['revol_util'].astype('float')
data['revol_util'].dtype

#I do not see the point of calculating every instance of month on which credit
#was granted, last payment made etc. since it's too complicated for not enough
#profit - drop

only_num_series = data.select_dtypes(include=np.number).columns.tolist()
all_series = []
for col in data.columns:
    all_series.append(col)
non_num_series = set(only_num_series) ^ set(all_series)
non_num_series
data.drop(axis=1, labels=['earliest_cr_line', 'int_rate', 'issue_d',
 'last_credit_pull_d', 'last_pymnt_d', 'loan_status', 'revol_util'],
 inplace=True)


 #export preprocessed file
 data.to_csv(r'credit_scoring_for_model_final.csv')

 #if needed for module export
 data
