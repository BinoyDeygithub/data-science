import pandas as pd
df = pd.DataFrame([[15, 12],
                    [33, 54],
                    [10, 32]], 
                    index = list('ABC'),
                    columns = list('DE'))


print(df)


print(df.loc[['A','C'],:])



import pandas as pd
df = pd.DataFrame([[15, 12],
                    [33, 54],
                    [10, 32]], 
                    index = ['one','two','three'],
                    columns = ['col1', 'col2'])
print(df)
#        col1  col2
# one      15    12
# two      33    54
# three    10    32
print(df.filter(regex = 'e$', axis = 0))      # row name ending with 'e'
#        col1  col2
# one      15    12
# three    10    32
print(df.filter(regex = '^c', axis = 1))      # column name starting with 'c'
#        col1  col2
# one      15    12
# two      33    54
# three    10    32 
              

import pandas as pd
df = pd.DataFrame([[15, 12],
                    [33, 54],
                    [10, 32]])
print(df[df >= 15])
#       0     1
# 0  15.0   NaN
# 1  33.0  54.0
# 2   NaN  32.0 
              
