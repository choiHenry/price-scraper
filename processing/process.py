import pandas as pd
from processing import utils

source = "../source/Prices.xlsx"

dfs = pd.ExcelFile(source)
print(dfs.sheet_names)

df = dfs.parse(sheet_name="Daily_Indexed", skiprows=8, index_col=3)
dfV2= df.drop(columns=['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2'])
dfV2['Time'] = dfV2.index
dfV3 = dfV2[['Time', 'US dollar', 'Euro', 'Korean won']]
dfV3.index = list(range(10596))
print(dfV3)
dfV3.to_csv('../data/XAUUSD.csv')
utils.pickle_object(dfV3, '../data/XAUUSD.pkl')