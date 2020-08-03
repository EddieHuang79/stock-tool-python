#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql

conn = pymysql.connect(
	host = '127.0.0.1', 
	user = 'root',
	passwd = "root",
	db = 'stock-tool',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cur = conn.cursor() 
cur.execute("SELECT * FROM stock_data WHERE stock_id = 820 AND data_date = '2020-04-15' LIMIT 1")

for r in cur: 
    print(r) 



cur.close() 
conn.close()


