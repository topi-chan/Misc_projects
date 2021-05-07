import pandas as pd
import numpy as np
import csv

data = pd.read_csv('credit_scoring_for_model.csv')

for col in data.columns:
    print(col)

data.applymap(np.isreal)

only_num_series = data.select_dtypes(include=np.number).columns.tolist()
all_series = []
for col in data.columns:
    all_series.append(col)
non_num_series = set(only_num_series) ^ set(all_series)
non_num_series

#still non numeric:
['earliest_cr_line',
 'int_rate',
 'issue_d',
 'last_credit_pull_d',
 'last_pymnt_d',
 'loan_status',
 'revol_util']
#int rate is percent, rest is date
