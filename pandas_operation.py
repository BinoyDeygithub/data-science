import pandas as pd
from openpyxl.workbook import Workbook
df=pd.DataFrame([[11,202],
                 [33,44]],
                 index=list("AB"),
                 columns=list("CD"))


df.to_excel('test.xlsx',sheet_name='Sheet1')

print(pd.read_excel("test.xlsx",'Sheet1'))


# import numpy as np
# import pandas as pd
# df = pd.read_table('chat.txt') 


import pandas as pd
import numpy as np

from xlsxwriter import Workbook

# Create the initial DataFrame
df = pd.DataFrame([[18, 10, 5, 11, -2],
                   [2, -2, 9, -11, 3],
                   [-4, 6, -19, 2, 1],
                   [3, -14, 1, -2, 8],
                   [-2, 2, 4, 6, 13]],
                  index=list('pqrst'),
                  columns=list('abcde'))

new_df=df[df.sum(axis=1)%2==0]

print(new_df)
          

with pd.ExcelWriter('file.xlsx',engine='xlsxwriter') as writer:
    new_df.to_excel(writer,sheet_name="sheet1")

df_temp=new_df.copy()
df_temp['m']=df_temp.apply(np.prod,axis=1)

with pd.ExcelWriter('file_df.xlsx', engine='xlsxwriter') as writer:
    new_df.to_excel(writer, sheet_name='Sheet1')
    df_temp.to_excel(writer, sheet_name='Sheet2')

