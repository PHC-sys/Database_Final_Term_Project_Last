from dbModule import Database
import pymysql
import sys
import pandas as pd
from delete_data import delete_data
from everyday_update import everyday_update, update_menu_management

db = Database()

everyday_update(db)
update_menu_management(db)

def log_in(db):
    while True:
        new_welcome = 'Welcome to Yonsei Buffet!\n' \
                      '=========================\n' \
                      'Service\n' \
                      '1. Log In\n' \
                      '2. Sign UP\n' \
                      '3. Exit\n' \
                      '=========================\n'
        print(new_welcome)
        answer = input('Select (1/2/3) : ')

        if answer == '1':
            id = input('ID: ')
            pw = input('PW: ')
            result = db.logcheck(id,pw)
            #print(result)
            if result is False:
                print('\nWrong Information. Please check again.\n')
            else:
                print('\n',result[1])
                customer_service(db)

        elif answer == '2':
            PhoneNumber = input('Enter your Phone Number: ')
            SchoolMail = input('Enter your Email: ')
            new_id = input('Your New ID: ')
            new_pw = input('Password: ')

            #Insert Database
            try:
                db.sign_up(PhoneNumber, new_id, new_pw, SchoolMail)
                print('\nComplete! Enjoy our Service!\n')

            except pymysql.err.OperationalError as e:
                print('\nOperationError: Enter correct value\n')

        elif answer == '3':
            print('Have a nice day!')
            db.close()
            sys.exit()
        else:
            print('\nYou put wrong input data. Please enter correct number.\n')

def customer_service(db):
    while True:
        service_page = 'How can I help you?\n' \
                       '===================\n' \
                       '1. Announcement\n' \
                       '2. Demand Survey\n' \
                       '3. Menu Evaluation\n' \
                       '4. Withdrawal\n' \
                       '5. Go Back\n' \
                       '===================\n'
        print(service_page)

        choice = input('Select (1/2/3/4/5): ')
        if choice == '1':
            title = 'Announcement\n' \
                    '==============================================================================\n'
            announcement = db.get_list('announcement','*')
            #recent_day = announcement[-1]['days']
            announcement = pd.DataFrame(announcement)
            #print(announcement)

            today_announcement = announcement.iloc[-2:]
            pd.set_option('display.max_columns', None)
            print(title)
            print(today_announcement,'\n')
            print('==============================================================================\n')
            i = True

            while i:
                print('\nEnter y when you want to go back')
                answer = input('Select (y): ')
                if answer == 'y':
                    break
                else:
                    pass
            customer_service(db)

        elif choice =='2':
            try:
                demand_survey(db)
            except :
                if pymysql.err.IntegrityError:
                    print('Error: Alreaday Submitted')
                else:
                    print('Error: Please enter correct input.')

        elif choice =='3':
            #Menu Evaluation
            try:
                menu_evaluation(db)
            except:
                if pymysql.err.IntegrityError:
                    print('Error: Alreaday Submitted')
                else:
                    print('Error: Please enter correct input.')

        elif choice =='4':
            result = delete_data(db, 'customer')
            if result is False:
                print('Please enter correct information\n')
                customer_service(db)
            else:
                print(f'Thank you for your use, {result}.')
            db.close()
            sys.exit()

        elif choice =='5':
            log_in(db)

        else:
            print('\nYou put wrong input data. Please enter correct number.\n')

def demand_survey(db):
    while True:
        demand_survey = 'Demand Survey\n' \
                        '=============\n' \
                        '1. Check Menu\n' \
                        '2. Survey\n' \
                        '3. Go Back\n' \
                        '=============\n'
        print(demand_survey)
        choice = input('Select (1/2/3): ')

        if choice == '1':
            n = True
            while n:
                options = 'Check Menu\n' \
                          '=========================\n' \
                          '1. Today\'s Menu\n' \
                          '2. 1 Week Menu From Today\n' \
                          '3. Go Back\n' \
                          '=========================\n'
                print(options)
                choice = input('Select (1/2/3): ')
                menu = db.get_list('menu_management', '*')

                if choice == '1':
                    menu = pd.DataFrame(menu)
                    today_menu = menu.iloc[-1]
                    print(today_menu)
                    i = True

                    while i:
                        print('\nEnter y when you want to go back')
                        answer = input('Select (y): ')
                        if answer == 'y':
                            break
                        else:
                            pass
                    break
                elif choice == '2':
                    menu = pd.DataFrame(menu)
                    week_menu = menu.iloc[-12:]
                    pd.set_option('display.max_columns', None)
                    print(week_menu)
                    i = True

                    while i:
                        print('\nEnter y when you want to go back')
                        answer = input('Select (y): ')
                        if answer == 'y':
                            break
                        else:
                            pass
                    break

                elif choice == '3':
                    break

                else:
                    print('\nYou put wrong input data. Please enter correct number.\n')

        elif choice == '2':
            survey = 'Please enter your score for each item\n' \
                     '=====================================\n'
            print(survey)
            id = input('Please enter your id: ')
            pw = input('Please enter your password: ')
            result = db.logcheck(id,pw)
            customerID = result[2]
            year = input('Year (yyyy): ')
            month = input('Month (mm): ')
            day = input('Day (dd): ')
            meal = input('Meal (l/d): ')
            rice = int(input('Rice_Preference (Score 1~5): '))
            soup = int(input('Soup_Preference (Score 1~5): '))
            noodle = int(input('Noodle_Preference (Score 1~5): '))
            main = int(input('Main_Preference (Score 1~5): '))
            side1 = int(input('Side1_Preference (Score 1~5): '))
            side2 = int(input('Side2_Preference (Score 1~5): '))
            kimchi = int(input('Kimchi_Preference (Score 1~5): '))
            total = input('Total_Preference (y/n): ')

            db.survey_submission(customerID, year, month, day, meal, rice, soup, noodle, main, side1, side2, kimchi, total)

        elif choice == '3':
            break
        else:
            print('\nYou put wrong input data. Please enter correct number.\n')

def menu_evaluation(db):
    while True:
        menu_evaluation = 'Menu Evaluation\n' \
                        '======================\n' \
                        '1. Evaluation_Taste\n' \
                        '2. Evaluation_Quantity\n' \
                        '3. Go Back\n' \
                        '======================\n'
        print(menu_evaluation)
        choice = input('Select (1/2/3): ')

        if choice == '1':
            evaluation_taste = 'Evaluation_Taste_Start\n' \
                               '======================\n' \

            print(evaluation_taste)
            id = input('Please enter your id: ')
            pw = input('Please enter your password: ')
            result = db.logcheck(id, pw)
            customerID = result[2]
            year = input('Year (yyyy): ')
            month = input('Month (mm): ')
            day = input('Day (dd): ')
            meal = input('Meal you ate (l/d): ')
            rice = int(input('Rice_Preference (Score 1~5): '))
            soup = int(input('Soup_Preference (Score 1~5): '))
            noodle = int(input('Noodle_Preference (Score 1~5): '))
            main = int(input('Main_Preference (Score 1~5): '))
            side1 = int(input('Side1_Preference (Score 1~5): '))
            side2 = int(input('Side2_Preference (Score 1~5): '))
            kimchi = int(input('Kimchi_Preference (Score 1~5): '))

            db.menu_evaluation_taste(customerID, year, month, day, meal, rice, soup, noodle, main, side1, side2, kimchi)

        elif choice == '2':
            evaluation_quantity = 'Evaluation_Quantity_Start\n' \
                                  '=========================\n'

            print(evaluation_quantity)
            id = input('Please enter your id: ')
            pw = input('Please enter your password: ')
            result = db.logcheck(id,pw)
            customerID = result[2]
            year = input('Year (yyyy): ')
            month = input('Month (mm): ')
            day = input('Day (dd): ')
            meal = input('Meal (l/d): ')
            rice = int(input('Rice_Preference (Score 1~5): '))
            soup = int(input('Soup_Preference (Score 1~5): '))
            noodle = int(input('Noodle_Preference (Score 1~5): '))
            main = int(input('Main_Preference (Score 1~5): '))
            side1 = int(input('Side1_Preference (Score 1~5): '))
            side2 = int(input('Side2_Preference (Score 1~5): '))
            kimchi = int(input('Kimchi_Preference (Score 1~5): '))

            db.menu_evaluation_quantity(customerID, year, month, day, meal, rice, soup, noodle, main, side1, side2, kimchi)

        elif choice == '3':
            break
        else:
            print('\nYou put wrong input data. Please enter correct number.\n')


log_in(db)