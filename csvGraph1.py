import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("temp.csv")
print (df)

fields = ['Name', 'Salary']
df1=pd.read_csv("temp.csv",skipinitialspace=True, usecols=fields)
df4=df1.groupby(['Name']).sum()
print (df4)
df4.plot.bar()
plt.show()

df2 = pd.DataFrame({'X' : ['B', 'B', 'A', 'A'], 'Y' : [1, 2, 3, 4]})
df3=df2.groupby(['X']).sum()
print (df3)