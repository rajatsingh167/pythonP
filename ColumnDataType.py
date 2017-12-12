import pandas as pd
df = pd.DataFrame()
print (df)

data = [1,2,3,4,5]
df = pd.DataFrame(data)
print (df)
print ( df.dtypes)

#For Column Different datatype
dtypes = {'Name':'string','Age':'int','Result':'string','Money':'Float'}
data = [['Alex',10 ,'Pass' ,1000.00],['Bob',12,'Fail',11],['Clarke',13,'pass',1]]
df = pd.DataFrame(data,columns=['Name','Age' ,'Result','Money'])
print (df)
print ( df['Age'].dtype)

#df.convert_objects(convert_numeric=True)
#df[['Age']] = df[['Age']].apply(pd.to_numeric)
#df.append('rank').astype('int')


#For Appending more column in dataframe
dtypes = {'Name':'string','Age':'int','Result':'string','Money':'Float'}
data = [['Alex',10 ,'Pass' ,1000.00],['Bob',12,'Fail',11],['Clarke',13,'pass',1]]
df = pd.DataFrame(data,columns=['Name','Age' ,'Result','Money'])
df['Rank']=[1,2,3]
print (df)
print ( df['Age'].dtype)
df['e'] = 0
print (df)

