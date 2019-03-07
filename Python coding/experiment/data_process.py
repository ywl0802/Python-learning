'''
程序框架：读取txt文件-按列将数据写入数据库-根据数据库依次读取并处理数据-将处理好的数据写入文件
细化需求：要得到一个Excel数据列表，数据顺序编号，时间（秒），压力数值
具体步骤：读取txt写入list，数据分类（时间和数值分开并编号），求值（16进制到10进制，注意补码），list写入多维数组，写入Excel
'''
#读取txt（16进制数据）文件，将数据按行以字符串形式保存入list中

def txt2list(txtname): #得到数据list
    data = []
    if not isinstance(txtname, str):
        txtname = str(txtname)
    #打开文件
    txt_content = open("D:\Program Files\Python coding\experiment\\" + txtname + ".txt","r")
    i = 0
    #读取文件
    for eachline in txt_content:
        i = i + 1
        data.append([i,eachline.split("]")[0],eachline.split("]")[1]])
    txt_content.close()
    #处理数据延迟————一条数据发成两行
    for elem in data:
        if len(elem[2]) <= 19:
            elem[2] = elem[2] + data[elem[0] + 1][2]    
            data.pop(elem[0] + 1)
    start_min = int(data[0][1].split(":")[-2])
    start_sec = int(data[0][1].split(":")[-1])
    #整理时间及压力数据
    for elem in data:
        time = ':'.join(elem[1].split(":")[3:6]) 
        sec = int(elem[1].split(":")[-1]) - start_sec + 60 * (int(elem[1].split(":")[-2]) - start_min)
        elem.append(time)
        elem.append(sec)
        if elem[2].split(" ")[3] == '00':
            tense = int(''.join(elem[2].split(" ")[3:7]),16)
        else:
            tense = int(''.join(elem[2].split(" ")[3:7]),16) - int("ffffffff",16)
        elem[2] = tense
    return data
    
#按list循环遍历将数据导入excel
import xlwt
import numpy as np
#创建工作簿
pre_data = txt2list(5)
i = 0
while i < len(pre_data):
    pre_data[i].append(i * 0.4)
    i = i + 1
data = np.array(pre_data)
book = xlwt.Workbook() 
print(data[1,...])
#创建表单
sheet1 = book.add_sheet(u'sheet1',cell_overwrite_ok=True)
#设置并写入表头
row0 = [u'序号', u'日期时间', u'压力值/g', u'测试时间', u'测试用时/s', u'精确时间/s']
for r in range(len(row0)):
    sheet1.write(0, r, row0[r])
#按i行j列顺序依次存入表格
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        sheet1.write(i+1,j,data[i][j])


book.save('D:/Program Files/Python coding/experiment/test_5.xls')


'''
小结：
list具有易于操作的特点，通过python的切片操作，极其适合处理少量数据
但是索引性能不如array强大，内存占用也比较大
下一步尝试使用数据库MySQL对数据进行保存，然后分步分批使用list处理
'''

