#assuming a dataframe/dataset is already present
#this is how we read/load IT
import pandas as pd

#jason=javaScript object notion
df=pd.read_json("data.json")
print(df)