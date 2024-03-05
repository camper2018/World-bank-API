
import requests
import json
from db.database import my_db

response = requests.get('http://api.worldbank.org/v2/lendingtypes?format=json')
parsed = response.content
data = json.loads(parsed)
print(data)

sql_formula = ('''INSERT INTO lending_types
                     (id,
                      iso2code,
                      value)
                     VALUES ( %(id)s, %(iso2code)s, %(value)s)
                  ''')
for l_type in data[1]:
    try:
        lending = dict()
        lending['id'] = l_type['id']
        lending['iso2code'] = l_type['iso2code']
        lending['value'] = l_type['value']
        print(lending)
        my_cursor = my_db.cursor()
        my_cursor.execute(sql_formula, lending)
        # my_db.commit()
    except Exception as e:
        print('Error: ', e)
my_cursor.close()
my_db.close()