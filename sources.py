import wbdata as wb
from db.database import my_db

countries = wb.get_country()
sources = wb.get_source()
topics = wb.get_topic()

sql_formula = ('''INSERT INTO sources
                     (id,
                      last_updated,
                      name,
                      code,
                      description,
                      url,
                      data_availability,
                      metadata_availability,
                      concepts
                      )
                     VALUES ( %(id)s, %(last_updated)s, %(name)s,%(code)s, %(description)s, 
                     %(url)s,%(data_availability)s, %(metadata_availability)s, %(concepts)s)
                  ''')
for source in sources:
    try:
        print(source)
        data = dict()
        data['id'] = source['id']
        data['last_updated'] = source['lastupdated']
        data['name'] = source['name']
        data['code'] = source['code']
        data['description'] = source['description']
        data['url'] = source['url']
        data['data_availability'] = source['dataavailability']
        data['metadata_availability'] = source['metadataavailability']
        data['concepts'] = source['concepts']
        print(data)
        my_cursor = my_db.cursor()
        my_cursor.execute(sql_formula, data)
        # my_db.commit()
    except Exception as e:
        print('Error: ', e)
my_cursor.close()
my_db.close()

