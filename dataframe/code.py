# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
bank = pd.DataFrame(bank_data)
print(bank.head())

#Code starts here

categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var.shape)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var.shape)

banks = pd.DataFrame(bank, columns = (bank.drop(['Loan_ID'], axis = 1, inplace = True)))

print(banks.isnull().sum().values.sum())

bank_mode = banks.mode()
banks.replace(np.nan, bank_mode, inplace = True)
print(banks.isnull().sum().values.sum())

avg_loan_amount = pd.pivot_table(banks, index = ['Gender', 'Married', 'Self_Employed'], values = 'LoanAmount') 
print(avg_loan_amount['LoanAmount'][1],2)
loan_approved_se = banks['Self_Employed'].value_counts()['Yes'] + banks['Loan_Status'].value_counts()['Y']

print(loan_approved_se)
loan_approved_nse = len(banks[banks['Self_Employed'] == 'No']) + len(banks[banks['Loan_Status'] == 'Y'])
print(loan_approved_nse)
_len = len(banks['Loan_Status']) 
print(_len)
percentage_se = loan_approved_se/_len * 100
print('%.2f' % percentage_se)


percentage_nse = loan_approved_nse/_len * 100
print('%.2f' % percentage_nse)

def convert(y):
    return int(y/12)
loan_term = banks['Loan_Amount_Term'].apply(lambda x: convert(x))
big_loan_term = len(banks[loan_term >= 25])
print(big_loan_term)


loan_groupby = banks.groupby('Loan_Status')[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()
print(mean_values.iloc[1,0])



