# -*- coding:utf-8 -*-
import sqlite3

# 连接数据库，如果数据库文件不存在则创建之
conn = sqlite3.connect('test.db')
# 创建游标
cursor = conn.cursor()
# 使用游标执行sql
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values(\'1\', \'Michael\')')
print(cursor.rowcount)
# 关闭游标
cursor.close()
# 提交事物
conn.commit()
# 关闭连接
conn.close()

## 查询:
conn2 = sqlite3.connect('test.db')
cursor = conn2.cursor()

cursor.execute('select * from user where id=?', ('1',))
# 获得查询结果集
values = cursor.fetchall()
print(values)
cursor.close()
conn2.close()