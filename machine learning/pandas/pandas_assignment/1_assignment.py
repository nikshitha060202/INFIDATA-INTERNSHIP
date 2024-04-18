import pandas as pd
data=pd.DataFrame({"name":['alice','bob','charlie'],
      "age":[25,30,35],
      "city":['new york','los angles','chicago']
       })
print(data)
data=pd.read_csv('person_info.csv')
print(data.shape)
print("statistical age:\n",data.describe())
print("info\n",data.info())
print(data.columns[data.isna().any()])
print(data.size)