import numpy as np
import pandas as pd
import xlwt,xlrd

'''
step1:读取Excel数据存入二维数组
step2:通过pandas画图
'''
workbook = xlrd.open_workbook(r'D:\Program Files\Python coding\experiment\test_2.xls')
sheet = workbook.sheet_by_name('sheet1')
pre_data = np.array()
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        pre_data.append(sheet.cell(row,col).value)
data = pd.DataFrame(pre_data,index = range(len(pre_data.shape[0])),columns=['index','date','tense','time','sec'])
print(data)

