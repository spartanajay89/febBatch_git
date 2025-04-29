import pandas as pd
from sqlalchemy import column

df=pd.read_csv('emp.csv')
print(df)
# df_dept=pd.read_csv("dept.csv")
# # print(df_dept)
#
# df_emp=pd.read_csv('emp.csv',header=3)
# print(df_emp)
# df_emp=pd.read_csv('emp.csv',usecols=['eno'])
# # df.to_csv("file_with_noheader")
# new_file=pd.read_csv("file_with_noheader.csv")
# print(new_file)


column('eno')
new=df[column]
print(new)
