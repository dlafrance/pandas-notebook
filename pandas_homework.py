import pandas as pd

# 2 Load DataFrame and explore
df_insurance = pd.read_csv('insurance.csv', header=0)

print(df_insurance.to_string())
print(f'Columns: \n', df_insurance.columns)
print(f'Index: \n', df_insurance.index)
print(f'Data types: \n', df_insurance.dtypes)
print(f'Shape: \n', df_insurance.shape)
print(f'Info: \n', df_insurance.info())
print(f'Describe: \n', df_insurance.describe())

# 3 Print column age
print(f'Age column \n', df_insurance['age'])

# 4 Print column age, children and charges
print(f'Age, children and charges columns \n', df_insurance[['age', 'children', 'charges']])

# 5 First 5 lines
print(f'First 5 lines \n', df_insurance[['age', 'children', 'charges']][0:5])

# 6 Charges functions
print(f'Average charges \n', df_insurance['charges'].mean())
print(f'Minimum charges \n', df_insurance['charges'].min())
print(f'Maximum charges \n', df_insurance['charges'].max())

# 7 Person that paid 10797.3362
print(f'Person: \n', df_insurance[['age', 'sex']][df_insurance['charges'] == 10797.3362])

# 8 Person that paid max charges
print(f'Age of person of max charge: \n', df_insurance['age'][df_insurance['charges'] == df_insurance['charges'].max()])

# 9 Count of insured people for each region
print(f'Count per region: \n', df_insurance['region'].value_counts())

# 10 Count of insured children
print(f'Insured children: \n', df_insurance['children'].sum())

# 11 Charges should be positively correlated with age as insurance is consumed more as we age. This is especially
# true for health insurance. The bmi and children fields should not be correlated. Just because a person has
# children, their BMI should not differ from those without children. Unless older people have a higher likelihood
# of having children in their insurance, and higher BMI can thus be associated with greater age.

#12 Correlation matrix
print(df_insurance.corr())