from generator import *
from dbModule import *

#db = Database()

def everyday_update(db):
    days = db.get_list('leftover','days')
    recent_day = days[-1]['days']
    today = datetime.now().date()
    days_interval = today.day - recent_day.day
    days_meal = days_meal_generator(days_interval)
    #print(days_interval)
    #print(days_meal)

    if days_interval == 0:
        return True
    else:
        for i in range(len(days_meal)):
            insert_sql = f"""INSERT INTO days_meal
            (Days, Meal)VALUES('{days_meal[i][0]}', '{days_meal[i][1]}');"""

            # print(insert_sql)
            try:
                db.execute(insert_sql)
                db.commit()
            except:
                pass

        days_meal_fk = db.get_list('days_meal','*')
        days_meal_fk = days_meal_fk[-len(days_meal):]
        leftover = initial_leftover_generator(days_meal_fk)
        menu_management = initial_menu_management_generator(days_meal_fk)
        print(days_meal_fk)

        for i in range(len(days_meal_fk)):
            insert_sql = f"""INSERT INTO leftover
                (Days, Meal, End_Weight, Actual_Demand, Leftover_per_person)
                VALUES('{leftover['Days'][i]}', '{leftover['Meal'][i]}','{leftover['End_Weight'][i]}','{leftover['Actual_Demand'][i]}','{leftover['Leftover_per_person'][i]}');"""

            # print(insert_sql)
            try:
                db.execute(insert_sql)
                db.commit()
            except:
                pass

            insert_sql = f"""INSERT INTO menu_management
                    (Days, Meal, Rice, Soup, Noodle, Main, Side1, Side2, Kimchi, Initial_Weight)
                    VALUES('{menu_management['Days'][i]}', '{menu_management['Meal'][i]}', '{menu_management['Rice'][i]}',
                    '{menu_management['Soup'][i]}','{menu_management['Noodle'][i]}','{menu_management['Main'][i]}',
                    '{menu_management['Side1'][i]}','{menu_management['Side2'][i]}','{menu_management['Kimchi'][i]}',
                    '{menu_management['Initial_Weight'][i]}');"""

            # print(insert_sql)
            try:
                db.execute(insert_sql)
                db.commit()
            except:
                pass

def update_menu_management(db):
    days_interval = 7
    #print(days_interval)
    days_meal = update_days_meal_generator(days_interval)
    #print(days_meal)

    for i in range(len(days_meal)):
        if i == 0 or i == 1 :
            pass
        else:
            insert_sql = f"""INSERT INTO days_meal
                (Days, Meal)VALUES('{days_meal[i][0]}', '{days_meal[i][1]}');"""

            # print(insert_sql)
            try:
                db.execute(insert_sql)
                db.commit()
            except:
                pass

    days_meal_fk = db.get_list('days_meal', '*')
    days_meal_fk = days_meal_fk[-(len(days_meal)-2):]
    #print(days_meal_fk)
    menu_management = initial_menu_management_generator(days_meal_fk)

    for i in range(len(days_meal_fk)):
        insert_sql = f"""INSERT INTO menu_management
                    (Days, Meal, Rice, Soup, Noodle, Main, Side1, Side2, Kimchi, Initial_Weight, Production_cost)
                    VALUES('{menu_management['Days'][i]}', '{menu_management['Meal'][i]}', '{menu_management['Rice'][i]}',
                    '{menu_management['Soup'][i]}','{menu_management['Noodle'][i]}','{menu_management['Main'][i]}',
                    '{menu_management['Side1'][i]}','{menu_management['Side2'][i]}','{menu_management['Kimchi'][i]}',
                    '{menu_management['Initial_Weight'][i]}','{menu_management['Production_cost'][i]}');"""

        # print(insert_sql)
        try:
            db.execute(insert_sql)
            db.commit()
        except:
            pass

    db.commit()


#everyday_update(db)
#update_menu_management(db)
#db.close()