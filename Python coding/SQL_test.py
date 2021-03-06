# -*- coding: utf-8 -*-

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")


#def get_score_in(low, high):
print(' 返回指定分数区间的名字，按分数从低到高排序 ')
    #先将三个数据都取出来，再用dict或tuple重排+提取实现

cursor.execute('select * from user where id=?', ('1', ))
values = cursor.fetchall()
print(values)
cursor.close()
conn.commit()
conn.close()
