import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import preprocessing
import matplotlib
import sklearn
import csv
import random
import statistics
import re


df = pd.read_csv('Loan_data.csv')
empty_col = []
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))
    if pct_missing == 1:
        empty_col.append(col)
print(empty_col)
df.head()

cols = df.columns
colours = ['#000099', '#ffff00']  # yellow is missing. blue is not missing
sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colours))
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
    return almost_empty_col


almost_empty_col = empty_check(df_minus_empty_col)
df = df_minus_empty_col

df_descr = pd.read_csv('LCDataDictionary.csv')
df_descr[df_descr.columns[:2]].head(n=10)
df_descr.drop(df_descr.columns[2:], axis=1, inplace=True)
df_descr.head()
df_descr.iloc[:1]

for col in df_descr.columns:
    print(col)


def print_description(col_name_list):
    loc = []
    for element in col_name_list:
        loc.append(df_descr.index[df_descr['LoanStatNew'] == element].tolist())
    for l in loc:
        print(df_descr.loc[l, 'Description'])


print_description(almost_empty_col)

df_descr.loc[50, 'Description']
df_descr.loc[52, 'Description']
df_descr.loc[58, 'Description']
df_descr.loc[145, 'Description']
df_descr.loc[146, 'Description']
df_descr.loc[147, 'Description']
df_descr.loc[148, 'Description']
df_descr.loc[149, 'Description']
df_descr.loc[150, 'Description']

# for l in loc:
#     print(df_descr.loc[l, 'LoanStatNew'])

df['mths_since_last_delinq'].head()
df['mths_since_last_delinq'].mean()
df['mths_since_last_delinq'].median()
df['mths_since_last_delinq'].max()
df['mths_since_last_delinq'].quantile([0.25, 0.5, 0.75])
df['mths_since_last_delinq'] = pd.qcut(df
                                       ['mths_since_last_delinq'].values, q=10).codes+1

df['mths_since_last_delinq'] = df['mths_since_last_delinq'].replace(to_replace=0,
                                                                    value=20)
df['mths_since_last_delinq'].head(n=25)


df['mths_since_last_record'].head()
df['mths_since_last_record'].mean()
df['mths_since_last_record'].median()
df['mths_since_last_record'].max()
df['mths_since_last_record'].quantile([0.25, 0.5, 0.75])
df['mths_since_last_record'] = pd.qcut(df['mths_since_last_record'].values,
                                       q=10, duplicates='drop').codes+1
df['mths_since_last_record'] = df['mths_since_last_record'].replace(to_replace=0,
                                                                    value=20)
df['mths_since_last_record'].mean()


df = df.drop(['next_pymnt_d', 'debt_settlement_flag_date', 'settlement_status',
              'debt_settlement_flag_date', 'settlement_date', 'settlement_amount',
              'settlement_percentage', 'settlement_term'], axis=1)


cols = df.columns[:30]
colours = ['#000099', '#ffff00']  # yellow is missing. blue is not missing
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
    df.at[i, 'desc'] = row_value

df['desc'].head(n=15)

cols = df.columns[29:]
colours = ['#000099', '#ffff00']  # yellow is missing. blue is not missing
sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colours))

empty_check(df)

df.loc[random.randrange(1, 40520), 'emp_title']
df.loc[random.randrange(1, 40520), 'emp_length']

emp_col = ['emp_title', 'emp_length']
print_description(emp_col)

df_descr.loc[20, 'Description']
df_descr.loc[19, 'Description']

for i, row in df['emp_length'].iteritems():
    row = str(row)
    if re.search("10", row):
        emp_lenght_value = 10
    elif re.findall("[1-9]", row):
        re_list = (re.findall("[1-9]", row))
        emp_lenght_value = int(re_list.pop(0))
    else:
        emp_lenght_value = 0
    df.at[i, 'emp_length'] = emp_lenght_value

df['emp_length'].head(n=25)

df = df.drop(['emp_title'], axis=1)


empty_check(df)

df.loc[random.randrange(1, 40520), 'pub_rec_bankruptcies']
print_description(['pub_rec_bankruptcies'])
df['pub_rec_bankruptcies'] = df['pub_rec_bankruptcies'].fillna(
    df['pub_rec_bankruptcies'].mean())

empty_check(df)

df['pub_rec_bankruptcies'].head(n=15)


# check if dataframe contains only numeric values
def numeric_check():
    str_elem = df.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all())
    only_numeric_elements = []
    for i, row in str_elem.iteritems():
        row = str(row)
        if row == 'False':
            only_numeric_elements.append(i)
    print(only_numeric_elements)


numeric_check()

df['id'].head(n=25)

df.applymap(lambda x: isinstance(x, (int, float)))

# these for which to_numeric returned true
df['id']
df['desc']
df['mths_since_last_delinq']
df['mths_since_last_record']
df['pub_rec_bankruptcies']

df.head(n=2)


for i, row in df['id'].iteritems():
    try:
        row = int(row)
    except:
        print(i, row)
df = df.drop(39786)

numeric_check()


def check_non_num_rows(col_name):
    for i, row in df[col_name].iteritems():
        try:
            row = int(row)
        except:
            print(i, row)


check_non_num_rows('term')


def check_consistency(column, *phrases):
    for i, row in df[column].iteritems():
        row = str(row)
        found = False
        for r in range(len(phrases)):
            if re.search(phrases[r], row):
                found = True
        if found != True:
            print(i, row)

check_consistency('term', '36 months', '60 months')
# change months into integers
for i, row in df['term'].iteritems():
    row = str(row)
    if re.search("36 months", row):
        term = 0
    elif re.search("60 months", row):
        term = 1
    df.at[i, 'term'] = term
# 0 = 36 months; 1 = 60 months; no other value is present

check_non_num_rows('int_rate')
# change % into floats
df['int_rate'].dtypes
# for i, row in df['term'].iteritems():
#     row = float(row)
#     print(row)
# maybe this will suffice? as data is hardly converted here
# TODO: check whether % values work with model

check_non_num_rows('grade')
# possibly leave it like that or change into integers for coherency and speed
# let's use hot encoding.

def hot_encoding(col):
    global df
    df = pd.concat([df.drop(col, axis=1), pd.get_dummies(df[col])], axis=1)
    return df

df = hot_encoding('grade')
df.head()

check_non_num_rows('sub_grade')
# as above
df = hot_encoding('sub_grade')
df.head()

check_non_num_rows('home_ownership')
# as above + check if there is any abbreviation from the rule
# MORTGAGE OWN RENT
check_consistency('home_ownership', 'MORTGAGE', 'OWN', 'RENT')

df.at[39786, 'home_ownership'] = 'NONE'
df = hot_encoding('home_ownership')


check_non_num_rows('annual_inc')
# set empty rows to mean or median or 0 or drop them
# df['annual_inc'].head(n=25)
# for i, row in df['annual_inc'].iteritems():
#     if row == 0.00:
#         print(i, row)
# df['annual_inc'].replace(to_replace=np.nan, value=0)
# dropping is probably a better idea, since nan may be missing value and may
# cloud a model
df = df.drop(labels=[39786, 42450, 42451, 42481, 42534])


check_non_num_rows('verification_status')
# check whether there are only 3 values and change them into integers
check_consistency('verification_status', 'Not Verified', 'Verified', 'Source Verified')
# ok!
df = hot_encoding('verification_status')

check_non_num_rows('issue_d')
# change into dates / numbers
df['issue_d'] = pd.to_datetime(df['issue_d'])
df['issue_d'] = df['issue_d'].dt.date
# changed into date, can it be properly understood by the model?

check_non_num_rows('loan_status')
# check whether there are only 2 values and change them into integers
#!! this is value to be predicted by the model!!
check_consistency('loan_status', 'Fully Paid',  'Charged Off')
#df = df.drop(labels=39786) dropped one empty row before - useless for the model
df = hot_encoding('loan_status')


check_non_num_rows('pymnt_plan')
# check if there is other value than "N" and if not - drop column
check_consistency('pymnt_plan', 'n')
df = df.drop(labels='pymnt_plan', axis=1)

check_non_num_rows('url')
# drop, seems irrelevant; also: url-s needs login, don't know if working
df = df.drop(labels='url', axis=1)

check_non_num_rows('purpose')
# assign randomly generated numbers for 'purpose' items or clean and hot encoding
row_list = []
for i, row in df['purpose'].iteritems():
    row_list.append(row)
list(set(row_list))
df['purpose'].fillna("other", inplace=True)
check_consistency('purpose', 'major_purchase', 'home_improvement',
                  'debt_consolidation', 'wedding', 'small_business', 'house', 'renewable_energy',
                  'car', 'credit_card', 'medical', 'educational', 'moving', 'other', 'vacation')
df = hot_encoding('purpose')

check_non_num_rows('title') # many values - drop?

title_series = df['title'].value_counts()
title_series.head(n=55)
title_series.head(n=55).sum()
consolidation = personal = home = medical = wedding = bussines = other = 0
for i, row in df['title'].iteritems():
    row = str(row)
    if re.search("consolidation", row, re.IGNORECASE):
        consolidation += 1
    elif re.search("personal", row, re.IGNORECASE):
        personal += 1
    elif re.search("home", row, re.IGNORECASE):
        home += 1
    elif re.search("medical", row, re.IGNORECASE):
        medical += 1
    elif re.search("wedding", row, re.IGNORECASE) or re.search("ring", row, re.IGNORECASE):
        wedding += 1
    elif re.search("business", row, re.IGNORECASE):
        bussines += 1
    else:
        other += 1
print(consolidation, personal, home, medical, wedding, bussines, other)
sum = consolidation + personal + home + medical + wedding + bussines + other
sum
df['title']
df['title'].isnull().values.any()
df['title'].isna().sum()
df['title'].fillna("other", inplace=True)

for i, row in df['title'].iteritems():
    row = str(row)
    if re.search("consolidation", row, re.IGNORECASE):
        row_value = "consolidation"
    elif re.search("personal", row, re.IGNORECASE):
        row_value = "personal"
    elif re.search("home", row, re.IGNORECASE):
        row_value = "home"
    elif re.search("medical", row, re.IGNORECASE):
        row_value = "medical"
    elif re.search("wedding", row, re.IGNORECASE) or re.search("ring", row, re.IGNORECASE):
        row_value = "wedding"
    elif re.search("business", row, re.IGNORECASE):
        row_value = "bussines"
    else:
        row_value = "other"
    df.at[i, 'title'] = row_value
df['title'].value_counts()
df = hot_encoding('title')


def generate_checklist(col):
    row_list = []
    for i, row in df[col].iteritems():
        row_list.append(row)
    print(list(set(row_list)))
    print(len(list(set(row_list))))


check_non_num_rows('zip_code')
# drop the 'xx'? check if it's relevant at all
generate_checklist('zip_code')
# dunno what to do with  it. 838 values but seems relevant.
# choosen - label encoding, as number of variables is substantial.
df['zip_code'] = preprocessing.LabelEncoder().fit_transform(df['zip_code'])
df.head()

check_non_num_rows('addr_state')
# assign into numbers
generate_checklist('addr_state')
# label encoding or hot encoding?
# TODO: choose encoding - atm: label encoding
df['addr_state'] = preprocessing.LabelEncoder().fit_transform(df['addr_state'])

check_non_num_rows('delinq_2yrs')
df['delinq_2yrs'].head(n=35)
# replace nan with median() value
df['delinq_2yrs'] = df['delinq_2yrs'].fillna(df['delinq_2yrs'].median())

check_non_num_rows('earliest_cr_line')
# change into dates
df['earliest_cr_line'] = pd.to_datetime(df['earliest_cr_line'])
df['earliest_cr_line'] = df['earliest_cr_line'].dt.date

check_non_num_rows('inq_last_6mths')
# it is important value; also there is a pattern - on last rows severas columns
# are missing - let's drop them for consistency (but check other columns first)
df.loc[42525]
df.loc[42526]
df = df.drop(df.index[42515:])

check_non_num_rows('open_acc')
# replace nan with mean() value or drop last columns - repeating 'nan' pattern
df['open_acc'].mean()
df['open_acc'].median()
df['open_acc'].std()
df['open_acc'] = df['open_acc'].fillna(df['open_acc'].median())

check_non_num_rows('pub_rec')
# as above
# repeating pattern of missing values for some records, eg. 42450 - drop.
df.drop(labels=[42460, 42473, 42484, 42495, 42510], inplace=True)

check_non_num_rows('revol_util')
# change % into floats
# TODO: check for 'int_rate' and apply same rules

check_non_num_rows('total_acc')
# replace nan with mean() value or drop last columns - repeating 'nan' pattern
df.drop(labels=[42515,42516,42517,42518], inplace=True)

check_non_num_rows('initial_list_status')
# investigate this column and its meaning
for i, row in df['initial_list_status'].iteritems():
    row = str(row)
    if row == "w":
        print(row)
    elif row != "f":
        print("Found something else!")
df['initial_list_status'].value_counts()
# column is "broken" - contains only 'f' values, hence is irrelevant
df.drop(columns='initial_list_status', inplace=True)

check_non_num_rows('last_pymnt_d')
# change into dates / numbers?
df['last_pymnt_d'] = pd.to_datetime(df['last_pymnt_d'])
df['last_pymnt_d'] = df['last_pymnt_d'].dt.date

check_non_num_rows('last_credit_pull_d')
# as above
df['last_credit_pull_d'] = pd.to_datetime(df['last_credit_pull_d'])
df['last_credit_pull_d'] = df['last_credit_pull_d'].dt.date

check_non_num_rows('collections_12_mths_ex_med')
# replace nan with mean() value or drop last columns - repeating 'nan' pattern
df['collections_12_mths_ex_med'].mean()
df['collections_12_mths_ex_med'].median()
df['collections_12_mths_ex_med'].std()
df['collections_12_mths_ex_med'].sum()
df['collections_12_mths_ex_med'] #empty column - drop
df.drop(columns='collections_12_mths_ex_med', inplace=True)

check_non_num_rows('application_type')
# check if there is other than "individual" and if not - drop column
generate_checklist('application_type')
df.drop(columns='application_type', inplace=True) #no other value - drop

check_non_num_rows('acc_now_delinq')
# replace nan with mean() value or drop last columns - repeating 'nan' pattern
#update: already solved by dropping above columns

check_non_num_rows('chargeoff_within_12_mths')
# replace nan with mean() value or drop last columns - repeating 'nan' pattern
# or maybe a median() value
df['chargeoff_within_12_mths'].mean()
df['chargeoff_within_12_mths'].median()
df['chargeoff_within_12_mths'].std()
df['chargeoff_within_12_mths'] #either null or nan - drop
df.drop(columns='chargeoff_within_12_mths', inplace=True)

check_non_num_rows('delinq_amnt')
# replace nan with mean() value or drop last columns - repeating 'nan' pattern
#update: already solved by dropping above columns

check_non_num_rows('tax_liens')
# replace nan with mean() value or drop last columns - repeating 'nan' pattern
df['tax_liens'].mean()
df['tax_liens'].median()
df['tax_liens'].std()
#it seems like an important feature - keep the column, fix nan's
df['tax_liens'].head(n=45)
generate_checklist('tax_liens')
check_consistency('tax_liens', '0.0', '1.0')
df['tax_liens'].value_counts()
#this column will be irrelevant for the model - single value '1' will be either
#in test or train data; though for larger database it could matter
df.drop(columns='tax_liens', inplace=True)

check_non_num_rows('hardship_flag')
# check if there is other than "N" and if not - drop column
df['hardship_flag'].value_counts()
df.drop(columns='hardship_flag', inplace=True)#single value present in column

check_non_num_rows('disbursement_method')
# check if there is other than "cash" and if not - drop column
df['disbursement_method'].value_counts()#single value present in column
df.drop(columns='disbursement_method', inplace=True)

check_non_num_rows('debt_settlement_flag')
# check if there is other than "cash" and if not - drop column
df['debt_settlement_flag'].value_counts()
df['debt_settlement_flag'] = df['debt_settlement_flag'].replace('Y', 1)
df['debt_settlement_flag'] = df['debt_settlement_flag'].replace('N', 0)

#id is irrelevant
df.drop(columns='id', inplace=True)

#checking if all values are numeric
if df.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all()) is True:
    print("All values are numeric!")
else:
    print("Something went wrong.")
df.applymap(np.isreal)
only_num_series = df.select_dtypes(include=np.number).columns.tolist()
all_series = []
for col in df.columns:
    all_series.append(col)
non_num_series = set(only_num_series) ^ set(all_series)
non_num_series

df['desc'].head(n=15)
df['desc'].value_counts()

df['earliest_cr_line'].head(n=15)
df['earliest_cr_line'].value_counts()

df['emp_length'].head(n=15)
df['emp_length'].value_counts()

df['int_rate'].head(n=15)
df['int_rate'].value_counts()

df['issue_d'].head(n=15)
df['issue_d'].value_counts()

df['last_credit_pull_d'].head(n=15)
df['last_credit_pull_d'].value_counts()

df['last_pymnt_d'].head(n=15)
df['last_pymnt_d'].value_counts()

df['revol_util'].head(n=15)
df['revol_util'].value_counts()

df['term'].head(n=15)
df['term'].value_counts()


#export preprocessed file
df.to_csv(r'credit_scoring_for_model.csv')

#if needed for module export
df
