import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()


df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
df.plot();



df=pd.DataFrame(np.random.rand(5,4),columns=['a','b','c','d'])
df.plot.bar()
plt.show()