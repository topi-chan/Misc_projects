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
data['earliest_cr_line'].value_counts()

data.drop(columns='int_rate', inplace=True)

y = data['loan_status'].values

x = data.drop(columns='loan_status')

x = (x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data)).values
