from datetime import datetime


#db = Database()

def delete_data(db, tableName):
    primary_keys = db.get_primary_keys_info(tableName)
    values = []
    print(primary_keys)
    for key in primary_keys:
        if key == 'Days':
            year = input('Year: ')
            month = input('Month: ')
            day = input('Day: ')
            date = year+'-'+month+'-'+day
            value = datetime.strptime(date, '%Y-%m-%d').date()
        elif key == 'CustomerID':
            id = input('ID: ')
            pw = input('Password: ')
            id_pw = {'Id': id, 'Password': pw}
            data = db.get_list('customer', 'Id', 'Password')
            if id_pw in data:
                delete_sql = f"""DELETE FROM {tableName} 
                WHERE Id = '{id}' and Password = '{pw}';"""
                db.execute(delete_sql)
                db.commit()
                print('Withdrawl Success!')
                return id
            else:
                print('Withdrawl Fail!')
                return False
        else:
            value = input(f'{key}: ')
        values.append(value)
    pk_dict = dict(zip(primary_keys, values))
    #print(pk_dict)
    n = len(primary_keys)
    delete_sql = f"""DELETE FROM {tableName} WHERE """
    for i in range(n):
        delete_sql += f"""{primary_keys[i]}='{values[i]}'"""
        if n-i ==1:
            delete_sql+=""";"""
        else:
            delete_sql+= """ and """
    #print(delete_sql)
    db.execute(delete_sql)
    db.commit()

    return pk_dict

'''
#Test Run

tableName = 'customer'

while True:
    try:
        deleted = delete_data(db,tableName)
        print('No more', deleted, 'in Database')
        break

    except:
        print('SyntaxError: Enter correct value')
        break
'''