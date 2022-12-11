import random, string
from datetime import datetime, timedelta

def customer_info_generator(id_length,pw_length, number):
    address = ['yonsei.ac.kr']

    string_pool = string.ascii_letters
    digit_pool = string.digits
    letter_pool = string_pool + digit_pool
    pw_pool = letter_pool

    email_address_list = []
    id_list = []
    phone_number_list = []
    pw_list = []

    for n in range(number):
        email_address = ""
        for i in range(id_length):
            email_address += random.choice(letter_pool)

        id_list.append(email_address)

        email_address += '@'
        email_address += random.choice(address)

        email_address_list.append(email_address)

    for n in range(number):
        pw = ""
        for i in range(pw_length):
            pw += random.choice(pw_pool)
        pw_list.append(pw)

    for n in range(number):
        phone_number = "010"
        phone_number += '-'

        for j in range(4):
            phone_number += random.choice(digit_pool)
        phone_number += '-'
        for m in range(4):
            phone_number += random.choice(digit_pool)
        phone_number_list.append(phone_number)


    customer_info = {'PhoneNumber':phone_number_list,'Id':id_list,'Password':pw_list,'SchoolMail':email_address_list}

    return customer_info

def days_meal_generator(days_interval):
    now = datetime.now().date()
    days = []
    for day in range(days_interval):
        before_n_day = now - timedelta(days=day)
        days.append(before_n_day)

    meal_pool = ['Lunch', 'Dinner']
    days_meal = []

    for day in range(days_interval):
        column_lunch = []
        column_dinner = []
        column_lunch.append(days[day])
        column_lunch.append(meal_pool[0])
        column_dinner.append(days[day])
        column_dinner.append(meal_pool[1])
        days_meal.append(column_lunch)
        days_meal.append(column_dinner)

    return days_meal

def update_days_meal_generator(days_interval):
    now = datetime.now().date()
    days = []
    for day in range(days_interval):
        before_n_day = now + timedelta(days=day)
        days.append(before_n_day)

    meal_pool = ['Lunch', 'Dinner']
    days_meal = []

    for day in range(days_interval):
        column_lunch = []
        column_dinner = []
        column_lunch.append(days[day])
        column_lunch.append(meal_pool[0])
        column_dinner.append(days[day])
        column_dinner.append(meal_pool[1])
        days_meal.append(column_lunch)
        days_meal.append(column_dinner)

    return days_meal

def initial_leftover_generator(days_meal):
    days_interval = len(days_meal)
    digit_pool = string.digits
    min_max_end_weight = 400
    max_min_end_weight = 2000
    max_max_end_weight = 3000
    min_actual_demand = 500
    max_actual_demand = 1000
    weight_unit = 'kg'
    cost_unit = 'won'
    leftover = {'Days':[],
                'Meal':[],
                'End_Weight': [],
                'Actual_Demand':[],#Actual_Demand = the number of sold coupons
                'Leftover_per_person': []}
    for day in range(days_interval):
        leftover['Days'].append(days_meal[day]['Days'])
        leftover['Meal'].append(days_meal[day]['Meal'])

        min_end_weight = random.randint(0, min_max_end_weight)
        max_end_weight = random.randint(max_min_end_weight, max_max_end_weight)
        end_weight = [min_end_weight,max_end_weight]
        end_weight = random.choices(end_weight, weights = [9,1])[0]
        leftover['End_Weight'].append(str(end_weight)+weight_unit)

        actual_demand = random.randint(min_actual_demand,max_actual_demand)
        leftover['Actual_Demand'].append(actual_demand)
        leftover['Leftover_per_person'].append(end_weight/actual_demand)

    return leftover

def initial_menu_management_generator(days_meal):
    days_interval = len(days_meal)
    min_initial_weight = 1000
    max_initial_weight = 1500
    weight_unit = 'kg'
    cost_per_unit = 7000
    Rice= ['흰쌀밥', '보리밥','콩밥','흑미밥']
    Soup= ['된장국','김치찌개','부대찌개','소고기무국','매운탕','미역국','꽃게탕','어묵국']
    Noodle= ['라면','짜장라면','우동','비빔면','잔치국수','카레라면']
    Main= ['소불고기','제육볶음','돈육김치볶음','돈까스','간장불백','떡볶이와 모듬튀김']
    Side1= ['콩나물무침','미나리무침','볶음김치','시금치무침','단무지무침','모듬나물']
    Side2= ['어묵볶음', '감자전', '김치전','애호박전','버섯볶음','고등어구이','삼치구이','갈치구이']
    Kimchi= ['배추김치','겉절이','파김치','갓김치','총각김치','깍두기',]

    menu_management = {'Days':[],
                        'Meal':[],
                        'Rice': [],
                        'Soup': [],
                        'Noodle':[],#Actual_Demand = the number of sold coupons
                        'Main': [],
                        'Side1': [],
                       'Side2': [],
                       'Kimchi': [],
                       'Initial_Weight': [],
                       'Production_cost': []}

    for day in range(days_interval):
        menu_management['Days'].append(days_meal[day]['Days'])
        menu_management['Meal'].append(days_meal[day]['Meal'])

        menu_management['Rice'].append(random.choice(Rice))
        menu_management['Soup'].append(random.choice(Soup))
        menu_management['Noodle'].append(random.choice(Noodle))
        menu_management['Main'].append(random.choice(Main))
        menu_management['Side1'].append(random.choice(Side1))
        menu_management['Side2'].append(random.choice(Side2))
        menu_management['Kimchi'].append(random.choice(Kimchi))

        initial_weight = random.randint(min_initial_weight, max_initial_weight)
        menu_management['Initial_Weight'].append(str(initial_weight)+weight_unit)
        menu_management['Production_cost'].append(str(initial_weight*cost_per_unit))

    return menu_management

def initial_demand_survey_generator(customer_id,days_meal):
    customer_number = len(customer_id)
    days_interval = len(days_meal)
    digit_pool = [1,2,3,4,5]

    menu_management = {'Days':[],
                        'Meal':[],
                       'CustomerID':[],
                       'Total_Preference':[],
                        'Rice_Preference': [],
                        'Soup_Preference': [],
                        'Noodle_Preference':[],
                        'Main_Preference': [],
                        'Side1_Preference': [],
                       'Side2_Preference': [],
                       'Kimchi_Preference': []}
    menu_keys = list(menu_management.keys())[4:]

    for day in range(days_interval):
        for customer in range(customer_number):
            menu_management['Days'].append(days_meal[day]['Days'])
            menu_management['Meal'].append(days_meal[day]['Meal'])
            menu_management['CustomerID'].append(customer_id[customer]['CustomerID'])
            sum = 0
            for key in menu_keys:
                score = int(random.choice(digit_pool))
                menu_management[key].append(score)
                sum += score

            if sum > 17.5:
                menu_management['Total_Preference'].append('YES')
            else:
                menu_management['Total_Preference'].append('NO')

    return menu_management

def initial_menu_evaluation_generator(customer_id,days_meal):
    customer_number = len(customer_id)
    days_interval = len(days_meal)
    digit_pool = [1,2,3,4,5]

    menu_evaluation_taste = {'Days':[],
                            'Meal':[],
                           'CustomerID':[],
                            'Rice_Preference_Taste': [],
                            'Soup_Preference_Taste': [],
                            'Noodle_Preference_Taste':[],
                            'Main_Preference_Taste': [],
                            'Side1_Preference_Taste': [],
                           'Side2_Preference_Taste': [],
                           'Kimchi_Preference_Taste': []}
    menu_evaluation_quantity = {'Days': [],
                            'Meal': [],
                            'CustomerID': [],
                            'Rice_Preference_Quantity': [],
                            'Soup_Preference_Quantity': [],
                            'Noodle_Preference_Quantity': [],
                            'Main_Preference_Quantity': [],
                            'Side1_Preference_Quantity': [],
                            'Side2_Preference_Quantity': [],
                            'Kimchi_Preference_Quantity': []}

    taste_keys = list(menu_evaluation_taste.keys())[3:]
    quantity_keys = list(menu_evaluation_quantity.keys())[3:]

    for day in range(days_interval):
        for customer in range(customer_number):
            menu_evaluation_taste['Days'].append(days_meal[day]['Days'])
            menu_evaluation_taste['Meal'].append(days_meal[day]['Meal'])
            menu_evaluation_taste['CustomerID'].append(customer_id[customer]['CustomerID'])
            menu_evaluation_quantity['Days'].append(days_meal[day]['Days'])
            menu_evaluation_quantity['Meal'].append(days_meal[day]['Meal'])
            menu_evaluation_quantity['CustomerID'].append(customer_id[customer]['CustomerID'])

            for key in taste_keys:
                taste_score = int(random.choice(digit_pool))
                menu_evaluation_taste[key].append(taste_score)

            for key in quantity_keys:
                quantity_score = int(random.choice(digit_pool))
                menu_evaluation_quantity[key].append(quantity_score)

    return menu_evaluation_taste, menu_evaluation_quantity
