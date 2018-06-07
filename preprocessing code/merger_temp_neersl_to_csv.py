
# coding: utf-8

# In[14]:


import pandas as pd
import pyexcel
import xlrd
import xlsxwriter

# writer class from module
writer = pd.ExcelWriter('tas_pr_1991_2015_USETHIS.xlsx', engine='xlsxwriter')


# collection of data

# precipitation data
pr = pd.read_excel('pr_1991_2015.xls', usecols = [0])

# temperature data
tas_t = pd.read_excel('tas_1991_2015.xls', usecols = [0])
# year
tas_y = pd.read_excel('tas_1991_2015.xls', usecols = [1])
# month
tas_m = pd.read_excel('tas_1991_2015.xls', usecols = [2])
# country
tas_c = pd.read_excel('tas_1991_2015.xls', usecols = [3])


# dataframe = pd.read_excel('tas_1991_2015.xls')

# dataframe['pr'] = pr

# old print statement, use to check output if uncertain of product
# print(dataframe)
# DataFrame.to_excel(excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0)
# write to excel

pr.to_excel(writer, 'sheet1',startcol = 0,index=True)
tas_t.to_excel(writer, 'sheet1',startcol = 2,index=False)
tas_y.to_excel(writer, 'sheet1',startcol = 3,index=False)
tas_m.to_excel(writer, 'sheet1',startcol = 4,index=False)
tas_c.to_excel(writer, 'sheet1',startcol = 5,index=False)

# save writer file
writer.save()

data_xls = pd.read_excel('tas_pr_1991_2015_USETHIS.xlsx', 'sheet1', index_col=None)
data_xls.to_csv('tas_pr_1991_2015_USETHIS.csv', encoding='utf-8', index=False)

