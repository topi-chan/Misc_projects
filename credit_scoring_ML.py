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

def print_description(col_name_list):
    loc = []
    for element in col_name_list:
        loc.append(df_descr.index[df_descr['LoanStatNew']==element].tolist())
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
    df.at[i,'emp_length'] = emp_lenght_value

df['emp_length'].head(n=25)

df = df.drop(['emp_title'], axis = 1)


empty_check(df)

df.loc[random.randrange(1, 40520), 'pub_rec_bankruptcies']
print_description(['pub_rec_bankruptcies'])
df['pub_rec_bankruptcies'] = df['pub_rec_bankruptcies'].fillna(
                             df['pub_rec_bankruptcies'].mean())

empty_check(df)

df['pub_rec_bankruptcies'].head(n=15)



#check if dataframe contains only numeric values
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

#these for which to_numeric returned true
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
            return (i, row)

check_non_num_rows('term')
#change months into integers
for i, row in df['term'].iteritems():
    row = str(row)
    if re.search("36 months", row):
        term = 0
    elif re.search("60 months", row):
        term = 1
    df.at[i,'term'] = term
#0 = 36 months; 1 = 60 months; no other value is present

check_non_num_rows('int_rate')
#change % into floats
df['int_rate'].dtypes
# for i, row in df['term'].iteritems():
#     row = float(row)
#     print(row)
#maybe this will suffice? as data is hardly converted here


check_non_num_rows('grade')
#possibly leave it like that or change into integers for coherency and speed
#let's use hot encoding.
df = pd.concat([df.drop('grade', axis=1), pd.get_dummies(df['grade'])], axis=1)
df.head()

check_non_num_rows('sub_grade')
#as above
df = pd.concat([df.drop('sub_grade', axis=1),
                                     pd.get_dummies(df['sub_grade'])], axis=1)
df.head()

check_non_num_rows('home_ownership')
#as above + check if there is any abbreviation from the rule
#MORTGAGE OWN RENT
for i, row in df['home_ownership'].iteritems():
    row = str(row)
    if re.search("MORTGAGE", row) or re.search("OWN", row) or re.search("RENT", row):
        pass
    else:
        print(i, row)
df.at[39786,'home_ownership'] = 'NONE'
df = pd.concat([df.drop('home_ownership', axis=1),
                                  pd.get_dummies(df['home_ownership'])], axis=1)



check_non_num_rows('annual_inc')
#set empty rows to mean or median or 0 or drop them
# df['annual_inc'].head(n=25)
# for i, row in df['annual_inc'].iteritems():
#     if row == 0.00:
#         print(i, row)
# df['annual_inc'].replace(to_replace=np.nan, value=0)
#dropping is probably a better idea, since nan may be missing value and may
#cloud a model
df = df.drop(labels=[39786, 42450, 42451, 42481, 42534])


def check_consistency(column, *phrases):
    for (i, row), p in zip(df[column].iteritems(), phrases):
        row = str(row)
        if re.findall(p, row):
                pass
#        if re.search(phrase, row) or re.search(phrase, row) or re.search(phrase, row) or re.search(phrase, row):
#            pass
        else:
            print(i, row)

check_non_num_rows('verification_status')
#check whether there are only 3 values and change them into integers
check_consistency('verification_status', 'Not Verified', 'Verified', 'Source Verified')

check_non_num_rows('issue_d')
#change into dates / numbers
check_non_num_rows('loan_status')
#check whether there are only 2 values and change them into integers
#!! this is value to be predicted by the model!!
check_non_num_rows('pymnt_plan')
#check if there is other value than "N" and if not - drop column
check_non_num_rows('url')
#drop, seems irrelevant
check_non_num_rows('purpose')
#assign randomly generated numbers for 'purpose' items
check_non_num_rows('title')
#drop?
check_non_num_rows('zip_code')
#drop the 'xx'?
check_non_num_rows('addr_state')
#assign into numbers
check_non_num_rows('delinq_2yrs')
df['delinq_2yrs'].head(n=35)
#replace nan with mean() value
check_non_num_rows('earliest_cr_line')
#change into dates / numbers
check_non_num_rows('inq_last_6mths')
#replace nan with mean() value
check_non_num_rows('open_acc')
#replace nan with mean() value or drop last columns - repeating 'nan' pattern
check_non_num_rows('pub_rec')
#as above
check_non_num_rows('revol_util')
#change % into floats
check_non_num_rows('total_acc')
#replace nan with mean() value or drop last columns - repeating 'nan' pattern
check_non_num_rows('initial_list_status')
#investigate this column and its meaning
check_non_num_rows('last_pymnt_d')
#change into dates / numbers?
check_non_num_rows('last_credit_pull_d')
#as above
check_non_num_rows('collections_12_mths_ex_med')
#replace nan with mean() value or drop last columns - repeating 'nan' pattern
check_non_num_rows('application_type')
#check if there is other than "individual" and if not - drop column
check_non_num_rows('acc_now_delinq')
#replace nan with mean() value or drop last columns - repeating 'nan' pattern
check_non_num_rows('chargeoff_within_12_mths')
#replace nan with mean() value or drop last columns - repeating 'nan' pattern
#or maybe a median() value
check_non_num_rows('delinq_amnt')
#replace nan with mean() value or drop last columns - repeating 'nan' pattern
check_non_num_rows('tax_liens')
#replace nan with mean() value or drop last columns - repeating 'nan' pattern
check_non_num_rows('hardship_flag')
#check if there is other than "N" and if not - drop column
check_non_num_rows('disbursement_method')
#check if there is other than "cash" and if not - drop column
check_non_num_rows('debt_settlement_flag')
#check if there is other than "cash" and if not - drop column


def change_column(col_name):
    for i, row in df[col_name].iteritems():
            row = str(row)
            if row == 0:
                row_value = 0
            elif row == row:
                row_value = 0.5
            elif row == row:
                row_value = 0.75
            else:
                row_value = 1
            df.at[i, col_name] = row_value












df['funded_amnt']
df['term']
str_elem.loc[str_elem[1] == 'False']

str_elem(df.iloc[:,1])
index = str_list.index(['False'])

for col in df.columns:
    for i, row in df[col].iteritems():
        row.to_numeric()
        # try:
        #     row.to_numeric()
        # except:
        #     Exception('Błąd!')

#df.iloc[:,50].fillna(0, inplace=True)

#df_empty = pd.DataFrame({'A' : []})
