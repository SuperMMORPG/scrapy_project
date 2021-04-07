import pymysql
import re

MYSQL_HOST = 'YOURS HOST'
MYSQL_USER = 'YOURS USER'
MYSQL_PASS = 'YOURS PASSWORD'
MYSQL_DB = 'YOURS DATABASE'

try:
    connection = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASS,
        db=MYSQL_DB,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
except Exception as e:
    print(e)

