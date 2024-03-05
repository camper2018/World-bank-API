import wbdata as wb
from db.database import my_db
# countries = wb.get_country()
sources = wb.get_source()
# for source in sources:
#     print(source)
# topics = wb.get_topic()


sql_formula = ('''INSERT INTO indicators
                     (id,
                      name,
                      unit,
                      source_id,
                      source_note,
                      source_organization
                      )
                     VALUES ( %(id)s, %(name)s, %(unit)s, %(source_id)s, %(source_note)s, %(source_organization)s)
                  ''')
for i in range(0, 2):
    source = sources[i]['id']
    print(int(source))
    indicator = wb.get_indicator(source=source)
    for item in indicator:
        try:
            print(item['id'])
            data = dict()
            data['id'] = item['id']
            data['name'] = item['name']
            data['unit'] = item['unit']
            data['source_id'] = item['source']['id']
            data['source_organization'] = item['sourceOrganization']
            data['source_note'] = item['sourceNote']
            my_cursor = my_db.cursor()
            my_cursor.execute(sql_formula, data)
            my_db.commit()
        except Exception as e:
            print('Error: ', e)
my_cursor.close()
my_db.close()



