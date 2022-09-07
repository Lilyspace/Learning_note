#从mySQL读取数据

import pymysql
host = 'localhost'
user = 'root'
password = 'Lily1234'
port = 3306

mysql = pymysql.connect (host = host, user = user, password = password)

cursor = mysql.cursor()

sql = "select * from lily.babynames where name = 'Jacob' or name = 'Emily'"

cursor.execute(sql)
results = cursor.fetchall()
print(results)
print(type(results))

cursor.close()
mysql.close()

#数据保存到excel
import pandas as pd
results = pd.DataFrame(results)
results.columns = ['Item','Name','BirthYear','Gender','Quantity']
results.set_index('Item')
print(results)

results.to_excel(r'D:\项目代码\Jacob&Emily.xls')


