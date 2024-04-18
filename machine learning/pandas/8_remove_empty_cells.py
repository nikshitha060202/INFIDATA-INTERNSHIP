import pandas as pd
df=pd.read_csv('data.csv') #loading the dataset
print('[info] data loaded sucessfully...')

print('[info]checking for NaN values...')
print(df.columns[df.isna().any()])

print('[info] removing NaN values..')
df=df.dropna() #this line remove entire row which has NaN Value

print('[info] checking for NaN values again...')
print(df.columns[df.isna().any()])