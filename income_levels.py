
import requests
import json
from db.database import my_db

response = requests.get('http://api.worldbank.org/v2/incomelevel?format=json')
parsed = response.content
data = json.loads(parsed)
print(data)


sql_formula = ('''INSERT INTO income_levels
                     (id,
                      iso2code,
                      value)
                     VALUES ( %(id)s, %(iso2code)s, %(value)s)
                  ''')
for income in data[1]:
    try:
        incomes = dict()
        incomes['id'] = income['id']
        incomes['iso2code'] = income['iso2code']
        incomes['value'] = income['value']
        my_cursor = my_db.cursor()
        my_cursor.execute(sql_formula, incomes)
        # my_db.commit()
    except Exception as e:
        print('Error: ', e)
my_cursor.close()
my_db.close()