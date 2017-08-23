import pandas as pd
from classes import Table

# t = Table('tables/idles_k1.csv')
# print(t.dataframe)

f = pd.DataFrame()
f = pd.read_csv('tables/idles_k1.csv')



print(f)
print('\n')
# print(f.ix[18,200])
print(f.loc[f.maximum_lump_size==18,'200'])
print(f.loc[f[f.columns[0]]==18,'200'])
print(f.columns[0])