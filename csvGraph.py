import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("temp.csv")
print (df)

df1=pd.read_csv("temp.csv",index_col=['Name'])

print (df1)
df1.plot.bar()
plt.show()



fields = ['Name', 'Salary']
df1=pd.read_csv("temp.csv",skipinitialspace=True, usecols=fields)

print (df1)
df1.plot.bar()
plt.show()