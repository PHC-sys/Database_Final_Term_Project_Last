# main.py
import sys,os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from dbModule import Database
from generator import *

db = Database()

def initialize(db):
    number = 8
    id_length = 8
    pw_length = 10
    customer_info = customer_info_generator(id_length, pw_length, number)

    days_interval = 10
    days_meal = days_meal_generator(days_interval)

    # print(customer_info)
    # print(customer_info['PhoneNumber'][0])

    delete_sql = f"""DELETE FROM menu_management"""
    db.execute(delete_sql)
    delete_sql = f"""DELETE FROM menu_evaluation_taste"""
    db.execute(delete_sql)
    delete_sql = f"""DELETE FROM menu_evaluation_quantity"""
    db.execute(delete_sql)
    delete_sql = f"""DELETE FROM leftover"""
    db.execute(delete_sql)
    delete_sql = f"""DELETE FROM demand_survey"""
    db.execute(delete_sql)
    delete_sql = f"""DELETE FROM customer"""
    db.execute(delete_sql)
    delete_sql = f"""DELETE FROM days_meal"""
    db.execute(delete_sql)
    db.commit()

    initialize_sql = '''alter table customer auto_increment = 1;'''
    db.execute(initialize_sql)
    db.commit()

    for i in range(number):
        insert_sql = f"""INSERT INTO customer
        (PhoneNumber, Id, Password, SchoolMail)VALUES('{customer_info['PhoneNumber'][i]}', '{customer_info['Id'][i]}', '{customer_info['Password'][i]}', '{customer_info['SchoolMail'][i]}');"""

        #print(insert_sql)
        db.execute(insert_sql)

    for i in range(len(days_meal)):
        insert_sql = f"""INSERT INTO days_meal
        (Days, Meal)VALUES('{days_meal[i][0]}', '{days_meal[i][1]}');"""

        # print(insert_sql)
        db.execute(insert_sql)

    customer_id_fk = db.get_list('customer', 'CustomerID')
    days_meal_fk = db.get_list('days_meal', '*')

    leftover = initial_leftover_generator(days_meal_fk)
    menu_management = initial_menu_management_generator(days_meal_fk)
    demand_survey = initial_demand_survey_generator(customer_id_fk, days_meal_fk)
    menu_evaluation_taste, menu_evaluation_quantity = initial_menu_evaluation_generator(customer_id_fk, days_meal_fk)

    for i in range(len(days_meal_fk)):
        insert_sql = f"""INSERT INTO leftover
            (Days, Meal, End_Weight, Actual_Demand, Leftover_per_person)
            VALUES('{leftover['Days'][i]}', '{leftover['Meal'][i]}','{leftover['End_Weight'][i]}','{leftover['Actual_Demand'][i]}','{leftover['Leftover_per_person'][i]}');"""

        # print(insert_sql)
        db.execute(insert_sql)

        insert_sql = f"""INSERT INTO menu_management
                (Days, Meal, Rice, Soup, Noodle, Main, Side1, Side2, Kimchi, Initial_Weight, Production_cost)
                VALUES('{menu_management['Days'][i]}', '{menu_management['Meal'][i]}', '{menu_management['Rice'][i]}',
                '{menu_management['Soup'][i]}','{menu_management['Noodle'][i]}','{menu_management['Main'][i]}',
                '{menu_management['Side1'][i]}','{menu_management['Side2'][i]}','{menu_management['Kimchi'][i]}',
                '{menu_management['Initial_Weight'][i]}', '{menu_management['Production_cost'][i]}');"""

        # print(insert_sql)
        db.execute(insert_sql)

    for i in range(len(days_meal_fk) * len(customer_id_fk)):
        insert_sql = f"""INSERT INTO demand_survey
            (Days, Meal, CustomerID, Total_Preference, Rice_Preference, Soup_Preference, Noodle_Preference, Main_Preference,
             Side1_Preference, Side2_Preference, Kimchi_Preference)
            VALUES('{demand_survey['Days'][i]}', '{demand_survey['Meal'][i]}','{demand_survey['CustomerID'][i]}',
            '{demand_survey['Total_Preference'][i]}',
            '{demand_survey['Rice_Preference'][i]}','{demand_survey['Soup_Preference'][i]}',
            '{demand_survey['Noodle_Preference'][i]}','{demand_survey['Main_Preference'][i]}',
            '{demand_survey['Side1_Preference'][i]}','{demand_survey['Side2_Preference'][i]}',
            '{demand_survey['Kimchi_Preference'][i]}');"""

        #print(insert_sql)
        db.execute(insert_sql)

        insert_sql = f"""INSERT INTO menu_evaluation_taste
                (Days, Meal, CustomerID, Rice_Preference_Taste, Soup_Preference_Taste, Noodle_Preference_Taste, Main_Preference_Taste,
                 Side1_Preference_Taste, Side2_Preference_Taste, Kimchi_Preference_Taste)
                VALUES('{menu_evaluation_taste['Days'][i]}', '{menu_evaluation_taste['Meal'][i]}','{menu_evaluation_taste['CustomerID'][i]}',
                '{menu_evaluation_taste['Rice_Preference_Taste'][i]}','{menu_evaluation_taste['Soup_Preference_Taste'][i]}',
                '{menu_evaluation_taste['Noodle_Preference_Taste'][i]}','{menu_evaluation_taste['Main_Preference_Taste'][i]}',
                '{menu_evaluation_taste['Side1_Preference_Taste'][i]}','{menu_evaluation_taste['Side2_Preference_Taste'][i]}',
                '{menu_evaluation_taste['Kimchi_Preference_Taste'][i]}');"""

        #print(insert_sql)
        db.execute(insert_sql)

        insert_sql = f"""INSERT INTO menu_evaluation_quantity
                    (Days, Meal, CustomerID, Rice_Preference_Quantity, Soup_Preference_Quantity, Noodle_Preference_Quantity, Main_Preference_Quantity,
                     Side1_Preference_Quantity, Side2_Preference_Quantity, Kimchi_Preference_Quantity)
                    VALUES('{menu_evaluation_quantity['Days'][i]}', '{menu_evaluation_quantity['Meal'][i]}','{menu_evaluation_quantity['CustomerID'][i]}',
                    '{menu_evaluation_quantity['Rice_Preference_Quantity'][i]}','{menu_evaluation_quantity['Soup_Preference_Quantity'][i]}',
                    '{menu_evaluation_quantity['Noodle_Preference_Quantity'][i]}','{menu_evaluation_quantity['Main_Preference_Quantity'][i]}',
                    '{menu_evaluation_quantity['Side1_Preference_Quantity'][i]}','{menu_evaluation_quantity['Side2_Preference_Quantity'][i]}',
                    '{menu_evaluation_quantity['Kimchi_Preference_Quantity'][i]}');"""

        #print(insert_sql)
        db.execute(insert_sql)

    db.commit()
    db.close()

initialize(db)
