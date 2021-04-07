import pandas as pd
import numpy as np
import matplotlib
import sklearn

"..."

df = pd.read_csv('Loan_data.csv')

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))
