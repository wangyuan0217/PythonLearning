from openpyxl import load_workbook
import pymysql
config = {
	'host': '121.5.20.129',
	'port':3306,
	'user': 'root',
	'password': '*****',
	'charset': 'utf8mb4',
}
conn = pymysql.connect(**config)
conn.autocommit(1)
cursor = conn.cursor()
name = 'python'
cursor.execute('create database if not exists %s' %name)
conn.select_db(name)
table_name = 'douban'
cursor.execute('create table if not exists %s(id MEDIUMINT NOT NULL AUTO_INCREMENT,name varchar(100),number varchar(30),score varchar(10),description varchar(200),primary key (id))'%table_name)

wb2 = load_workbook('电影.xlsx')
ws=wb2.get_sheet_names()
for row in wb2:
	print("1")
	for cell in row:
		value1=(cell[0].value,cell[1].value,cell[2].value,cell[3].value)
		cursor.execute('insert into douban (name,number,score,description) values(%s,%s,%s,%s)',value1)

print("overing...")
# for row in A:
# 	print(row)
#print (wb2.get_sheet_names())