import pandas as pd
import numpy as np
import csv

data = pd.read_csv('credit_scoring_for_model.csv')

for col in data.columns:
    print(col)


y = data['loan_status'].values

x = data.drop(columns='loan_status')

x = (x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data)).values
