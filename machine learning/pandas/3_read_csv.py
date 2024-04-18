#assuming a dataframe/dataset is already present,
# this is how we read/load it

import pandas as pd #for creating and handling dataframe
#loading id.csv into pandas dataframe
data=pd.read_csv("diabetes.csv")
print(data)#displaying the dataframe