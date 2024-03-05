
# import wbdata as wb
import requests
import json
from db.database import my_db

# countries = wb.get_country()
for i in range(2, 8):
    response = requests.get('http://api.worldbank.org/v2/country/all?format=json&page=%d' % i)
    parsed = response.content
    countries = json.loads(parsed)
    sql_formula = ('''INSERT INTO countries
                         (id,
                          iso2code,
                          name,
                          region_id,
                          admin_region,
                          income_level_id,
                          lending_type_id,
                          capital_city,
                          longitude,
                          latitude)
                         VALUES ( %(id)s, %(iso2code)s, %(name)s, %(region_id)s,%(admin_region)s, %(income_level_id)s, 
                         %(lending_type_id)s, %(capital_city)s, %(longitude)s,%(latitude)s)
                      ''')

    for country in countries[1]:
        try:
            data = dict()
            data['id'] = country['id']
            data['iso2code'] = country['iso2Code']
            data['name'] = country['name']
            data['region_id'] = country['region']['id']
            data['admin_region'] = country['adminregion']['value']
            data['income_level_id'] = country['incomeLevel']['id']
            if country['lendingType']['id']:
                data['lending_type_id'] = country['lendingType']['id']
            else:
                data['lending_type_id'] = 'NA'
            data['capital_city'] = country['capitalCity']
            data['longitude'] = country['longitude']
            data['latitude'] = country['latitude']
            my_cursor = my_db.cursor()
            my_cursor.execute(sql_formula, data)
            # my_db.commit()
        except Exception as e:
            print('Error: ', e)

my_cursor.close()
my_db.close()












