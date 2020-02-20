# Load dataset
import pandas as pd

nhl = pd.read_excel(io='nhl_player_data.xlsx',
                    sheet_name='nhl_player_data',
                    header=0)

# Information and summary stats
print(f'Columns: \n', nhl.columns)
print(f'Index: \n', nhl.index)
print(f'Data types: \n', nhl.dtypes)
print(f'Shape: \n', nhl.shape)
print(f'Info: \n', nhl.info())
print(f'Describe: \n', nhl.describe())

# Correlations
print(nhl.corr())

# Insight
# The average age of NHL players has remained stable since 2004
print(nhl.groupby('Season')['Age'].mean())\

# Penalty minutes have declined over the past 10 years. However I do notice that data for 2009 seems corrupt. After
# some investigation I could see duplication for each player during that year. They are not exactly duplicates
# as the figures are different. It's actually the 2007 figures being duplicated for 2009.
# I may need to use the data set only from 2010 onwards or find a way to eliminate the duplicate...
print(nhl.groupby('Season')[['G', 'PIM']].sum())
