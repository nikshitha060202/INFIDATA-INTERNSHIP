# assuming the dataframe/dataset is already present
#this is how we read/load IT

import pandas as pd #for creating and handling dataframe
#loading id.csv into pandas dataframe
data=pd.read_csv("diabetes.csv")
print(data) # displaying the dataframe

#
print("displaying specific columns")
print(data['Glucose']) #displaying single column
print(data[["Glucose","BMI"]]) #displaying multiple column

#
print(data.shape) #displaying shape of datasets

print(data.size) #displaying size of data

#indexing
print(data.head()) #print first 5 rows of data

print(data.tail()) #print last 5 rows of data
