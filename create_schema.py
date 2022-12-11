from dbModule import *

def create_schema():
    try:
        db = pymysql.connect(
            user='root',
            port=3306,
            password=password,
            host='127.0.0.1',
            charset='utf8'
        )

        cursor = db.cursor()
        sql_create = 'CREATE DATABASE TermProject'
        cursor.execute(sql_create)
    except:
        pass

create_schema()

def create_tables(filename):
    dbName = 'TermProject'
    db = pymysql.connect(
        user='root',
        port=3306,
        password=password,
        db = dbName,
        host='127.0.0.1',
        charset='utf8'
    )
    cursor = db.cursor()

    sql = open(filename, 'r',encoding='utf8').read()

    for statement in sql.split(';'):
        print(len(statement))
        if len(statement) > 5:
            cursor.execute(statement + ';')
'''
try:
    create_tables('Create-Table-View-Procedure-Termproject.sql')
except:
    print('Error: Already exists')
'''