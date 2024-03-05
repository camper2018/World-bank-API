
import requests
import json
from db.database import my_db


response = requests.get('http://api.worldbank.org/v2/region?format=json')
parsed = response.content
regions_data = json.loads(parsed)
sql_regions = ('''INSERT INTO regions
                 (id,
                 iso2code,
                 value)
                 VALUES ( %(id)s, %(iso2code)s, %(value)s)
              ''')

for region in regions_data[1]:
    try:
        regions = dict()
        regions['id'] = region['code']
        regions['iso2code'] = region['iso2code']
        regions['value'] = region['name']
        my_cursor = my_db.cursor()
        my_cursor.execute(sql_regions, regions)
        # my_db.commit()
    except Exception as e:
        print('Error: ', e)

my_cursor.close()
my_db.close()
