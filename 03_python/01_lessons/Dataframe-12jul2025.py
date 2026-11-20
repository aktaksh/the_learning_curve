#.     Product  Price  Quantity  Revenue
#0       A     10         2       20
#1       B     20         5      100
#2       C     30         3       90
#3       D     40         4      160

import numpy as np
import pandas as pd
df1 = pd.DataFrame({"Product":["A","B","C","D"], "Price":[10,20,30,40], "Quantity":[2,5,3,4]})
print(df1["Price"])
print(df1.head(1)["Price"])

df1["Revenue"] = np.array(df1["Price"]) * np.array(df1["Quantity"])
print(df1["Revenue"])
print(df1.head(2))
print(df1.tail(1))

print(df1.info())
#head tail and shape uses () as they are pandas functions

print(df1.shape) 
print(df1.columns)
#shape and  column doest use () as they are inbuilt functions

print(df1.describe())

# identifier is smallest token







#Numpy small bracket
#dataframe Square bracket
#Function comes in classes and always user defined
#Method is subset of Libraries

