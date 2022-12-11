import pymysql
import os
from sandbox import converter
from datetime import datetime

dbName = 'TermProject'
password = os.environ.get('MYSQLPW')

class Database():
    def __init__(self):
        self.db= pymysql.connect(host='localhost', port= 3306,
                                  user='root',
                                  password=password,
                                  db=dbName,
                                  charset='utf8')
        self.cursor= self.db.cursor(pymysql.cursors.DictCursor)
        '''
        sql_create = 'CREATE DATABASE TermProject'
        sql_use = 'USE TermProject'
        cursor.execute(sql_create)
        cursor.execute(sql_use)
        #테이블 생성
        sql = open("DBP-e14-MySQL-VRG-Create-Tables.sql").read()
        #데이터 생성
        sql = open("DBP-e14-MySQL-VRG-Insert-Data.sql").read()
        for statement in sql.split(';'):
            if len(statement) > 5:
            cursor.execute(statement + ';')
        '''

    def logcheck(self,id,password):
        sql = "select CustomerID from customer WHERE Id=%s AND Password = %s"
        result = self.cursor.execute(sql, (id, password))
        #print(id,password)
        welcome = f'Hello {id}, Successfully Logged In!'
        if result == 0:
            return False
        else :
            customerID = dict(self.cursor.fetchone())['CustomerID']
            return True,welcome, customerID

    def get_list(self, TableName, *columnName):
        columnNames = converter(*columnName)
        sql =f"""select {columnNames} 
                from {TableName};"""
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def get_primary_keys_info(self, tablename):
        sql = f"""SHOW keys
                    FROM {tablename}
                    WHERE Key_name = 'PRIMARY';"""
        self.cursor.execute(sql)
        keys_info = self.cursor.fetchall()
        n = len(keys_info)
        primary_keys = []
        for i in range(n):
            primary_keys.append(keys_info[i]['Column_name'])

        return primary_keys

    def sign_up(self,PhoneNumber, id, password, SchoolMail):
        sql = f"""INSERT INTO customer
        (PhoneNumber, Id, Password, SchoolMail)VALUES('{PhoneNumber}','{id}', '{password}','{SchoolMail}');"""
        self.cursor.execute(sql)
        self.db.commit()

    def survey_submission(self,id, year, month, day, meal, rice, soup, noodle, main, side1, side2, kimchi, total):
        days = year + '-' + month + '-' + day
        days = datetime.strptime(days, '%Y-%m-%d').date()

        if meal == 'l':
            meal = 'Lunch'
        elif meal == 'd':
            meal = 'Dinner'
        else:
            print('Error: Enter correct input (l/d).')

        if total == 'y':
            total = 'YES'
        elif total == 'n':
            total = 'NO'
        else:
            print('Error: Enter correct input (y/n).')

        sql = f"""INSERT INTO demand_survey
                (Days, Meal, CustomerID, Total_Preference, Rice_Preference, Soup_Preference, Noodle_Preference, 
                Main_Preference, Side1_Preference, Side2_Preference, Kimchi_Preference)
                VALUES('{days}','{meal}', '{id}','{total}','{rice}','{soup}','{noodle}','{main}','{side1}',
                '{side2}','{kimchi}');"""
        self.cursor.execute(sql)
        self.db.commit()
        print('Thank you for your Submission')

    def menu_evaluation_taste(self,id, year, month, day, meal, rice, soup, noodle, main, side1, side2, kimchi):
        days = year + '-' + month + '-' + day
        days = datetime.strptime(days, '%Y-%m-%d').date()

        if meal == 'l':
            meal = 'Lunch'
        elif meal == 'd':
            meal = 'Dinner'
        else:
            print('Error: Enter correct input (l/d).')

        sql = f"""INSERT INTO menu_evaluation_taste
                (Days, Meal, CustomerID, Rice_Preference_Taste, Soup_Preference_Taste, Noodle_Preference_Taste, 
                Main_Preference_Taste, Side1_Preference_Taste, Side2_Preference_Taste, Kimchi_Preference_Taste)
                VALUES('{days}','{meal}', '{id}','{rice}','{soup}','{noodle}','{main}','{side1}',
                '{side2}','{kimchi}');"""
        self.cursor.execute(sql)
        self.db.commit()
        print('Thank you for your Submission')

    def menu_evaluation_quantity(self,id, year, month, day, meal, rice, soup, noodle, main, side1, side2, kimchi):
        days = year + '-' + month + '-' + day
        days = datetime.strptime(days, '%Y-%m-%d').date()

        if meal == 'l':
            meal = 'Lunch'
        elif meal == 'd':
            meal = 'Dinner'
        else:
            print('Error: Enter correct input (l/d).')

        sql = f"""INSERT INTO menu_evaluation_quantity
                (Days, Meal, CustomerID, Rice_Preference_Quantity, Soup_Preference_Quantity, Noodle_Preference_Quantity, 
                Main_Preference_Quantity, Side1_Preference_Quantity, Side2_Preference_Quantity, Kimchi_Preference_Quantity)
                VALUES('{days}','{meal}', '{id}','{rice}','{soup}','{noodle}','{main}','{side1}',
                '{side2}','{kimchi}');"""
        self.cursor.execute(sql)
        self.db.commit()
        print('Thank you for your Submission')

    def update_work(self,TransactionID,CustomerID,DateSold,SalesPrice):
        sql= "UPDATE trans SET DateSold=%s, SalesPrice=%s, CustomerID = %s WHERE TransactionID =%s ;"
        result = self.cursor.execute(sql,(DateSold, SalesPrice, CustomerID, TransactionID))
        self.db.commit()

    def execute(self, query, args={}):
        self.cursor.execute(query, args) 
 
    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row= self.cursor.fetchone()
        return row
 
    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row= self.cursor.fetchall()
        return row
 
    def commit(self):
        self.db.commit()

    def close(self):
        self.db.close()

