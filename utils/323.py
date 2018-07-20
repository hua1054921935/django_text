#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:python
# datetime:18-7-8 下午6:39
# software: PyCharm
import pymysql
# PY_MYSQL_CONN_DICT = {
#     "host": '39.107.112.244',
#     "port": 3306,
#     "user": 'python',
#     "passwd": '123456',
#     "db": 'Teachers',
#     'charset': 'utf8',
# }
sql_one = """SELECT count(*) AS many,state FROM b_case GROUP BY state;"""
sql_two = """SELECT count(*) AS many,field_oriented FROM b_case GROUP BY field_oriented;"""
# conn=pymysql.connect(host='39.107.112.244', port=3306, user='python', password='123456',db='Teachers', charset='ut8')
# cursor=conn.cursor()
# cursor.execute(sql_one)
# data=cursor.fetchall()
# cursor=conn.cursor()
# cursor.execute(sql_two)
# datas=cursor.fetchall()
# print(data,datas)
import pymysql

conn = pymysql.connect(host='192.168.125.12', port=3306, user='root', passwd='iiecas',db='bc')

with conn.cursor() as cursor:
    cursor.execute(sql_one)
    # cursor.execute(sql_two)
    result = cursor.fetchall()
    print(result)

# with conn.cursor() as cursor:
    # cursor.execute(sql_one)
    cursor.execute(sql_two)
    result = cursor.fetchall()
    print(result)

# cursor.close()
#
# conn.close()
