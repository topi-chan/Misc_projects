import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib, sklearn, csv, random, statistics, re


df = pd.read_csv('Loan_data.csv')
empty_col = []
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))
    if pct_missing == 1:
        empty_col.append(col)
print(empty_col)
df.head()

cols = df.columns[:]
colours = ['#000099', '#ffff00'] # yellow is missing. blue is not missing
sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colours))
print(empty_col)
df_minus_empty_col = df.drop(empty_col, axis=1)

print(df_minus_empty_col.head(n=20))

def empty_check(df_instance):
    almost_empty_col = []
    for col in df_instance.columns:
        pct_missing = np.mean(df[col].isnull())
        value = float(np.mean(df[col].isnull()))
        print('{} - {}%'.format(col, round(pct_missing*100)))
        if round(pct_missing) == 1:
            almost_empty_col.append(col), almost_empty_col.append(value)
    print(almost_empty_col)
empty_check(df_minus_empty_col)
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
df['mths_since_last_delinq'].mean()
df['mths_since_last_delinq'].median()
df['mths_since_last_delinq'].max()
df['mths_since_last_delinq'].quantile([0.25,0.5,0.75])
df['mths_since_last_delinq'] = pd.qcut(df
                              ['mths_since_last_delinq'].values, q = 10).codes+1

df['mths_since_last_delinq'] = df['mths_since_last_delinq'].replace(to_replace
                                                            = 0, value = 20)
df['mths_since_last_delinq'].head(n=25)


df['mths_since_last_record'].head()
df['mths_since_last_record'].mean()
df['mths_since_last_record'].median()
df['mths_since_last_record'].max()
df['mths_since_last_record'].quantile([0.25,0.5,0.75])
df['mths_since_last_record'] = pd.qcut(df['mths_since_last_record'].values,
                               q = 10, duplicates='drop').codes+1
df['mths_since_last_record'] = df['mths_since_last_record'].replace(to_replace
                                                            = 0, value = 20)
df['mths_since_last_record'].mean()


df = df.drop(['next_pymnt_d', 'debt_settlement_flag_date', 'settlement_status',
        'debt_settlement_flag_date', 'settlement_date', 'settlement_amount',
        'settlement_percentage', 'settlement_term'], axis = 1)


cols = df.columns[:30]
colours = ['#000099', '#ffff00'] # yellow is missing. blue is not missing
sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colours))

df['desc'].head()
df.loc[random.randrange(1, 40520), 'desc']
# borrowers with description seems more reliable, as they care enough to provide
# valid reason for taking a loan; let's try to assign value up to 1 to borrowers
# with description and 0 to ones with no description.
# (assuming the description avaibility depends on the lender, but stil we can
# analyse description lenght)
max_str_len = 0
sum_str_len = 0
list_for_median = []
for row in df['desc']:
    row = str(row)
    row_len = len(row)
    sum_str_len += row_len
    list_for_median.append(row_len)
    if row_len > max_str_len:
        max_str_len = len(row)
print(max_str_len)
sum_str_len
mean_str_len = sum_str_len / 40520
print(mean_str_len)
str_median_len = statistics.median(list_for_median)
print(str_median_len)

for i, row in df['desc'].iteritems():
    row = str(row)
    row_len = len(row)
    if row_len == 0:
        row_value = 0
    elif row_len <= str_median_len:
        row_value = 0.5
    elif row_len <= mean_str_len:
        row_value = 0.75
    else:
        row_value = 1
    df.at[i,'desc'] = row_value

df['desc'].head(n=15)

cols = df.columns[29:]
colours = ['#000099', '#ffff00'] # yellow is missing. blue is not missing
sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colours))

empty_check(df)

df.loc[random.randrange(1, 40520), 'emp_title']
df.loc[random.randrange(1, 40520), 'emp_length']

loc = []
loc.append(df_descr.index[df_descr['LoanStatNew']=='emp_title'].tolist())
loc.append(df_descr.index[df_descr['LoanStatNew']=='emp_length'].tolist())
for l in loc:
    print(df_descr.loc[l, 'Description'])
df_descr.loc[20, 'Description']
df_descr.loc[19, 'Description']

for i, row in df['emp_length'].iteritems():
    row = str(row)
    if re.search("10", row):
        emp_lenght_value = 10
    elif re.findall("[1-9]", row):
        re_list = (re.findall("[1-9]", row))
        emp_lenght_value = re_list.pop(0)
    else:
        emp_lenght_value = 0
    df.at[i,'emp_length'] = emp_lenght_value

df['emp_length'].head(n=25)

df = df.drop(['emp_title'], axis = 1)


empty_check(df)

#df.iloc[:,50].fillna(0, inplace=True)

#df_empty = pd.DataFrame({'A' : []})
