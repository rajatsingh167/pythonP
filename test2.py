import pandas as pd
s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
#retrieve the last three element
print(s[-3:])