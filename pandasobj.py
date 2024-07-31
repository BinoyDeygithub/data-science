import pandas as pd
lst= [{'c1':1,'c2':2},
      {'c1':5,'c2':10,"c3":15}]

print(pd.DataFrame(lst,index=['R1','R2']))

dc={'c1':['1','3'],
    'c2':['6','8']
    }

print(pd.DataFrame(dc, index=['r1','r2']))


lst=[[23,45],[23,67]]
print(pd.DataFrame(lst,index=list('pq'),columns=list('ab')))



df = pd.DataFrame({'A': [10., 20.],
                    'B': "text",
                    'C': [2,60],
                    'D': 3+9j})
print(df)
print(df.dtypes)

print(df.info())
print(df.index)
print(df.columns)

import pandas as pd
import numpy as np

# Create the initial DataFrame
df = pd.DataFrame([[0.23,'f1'],[5.36,'f2']],
                  index = list('pq'),
                  columns = list('ab'))
print(df)
df.rename(columns={'a':'A','b':'B'},inplace= True)
print(df)

df['c']=np.random.random(len(df))
print(df)


df['A']=df["A"].astype(complex)

lst = ['f30', 'f50', 'f2', 'f0']
matching_row=df[df.isin(lst).any(axis=1)]
print(matching_row)