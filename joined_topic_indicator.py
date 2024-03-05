import wbdata as wb
from db.database import my_db

sources = wb.get_source()

sql_formula = ('''INSERT INTO indicator_topic_union
                     (topic_id,
                      indicator_id
                      )
                     VALUES (%(topic_id)s, %(indicator_id)s)
 
                  ''')

for i in range(0, 2):
    source = sources[i]['id']
    indicator = wb.get_indicator(source=source)
    for item in indicator:
        try:
            # print(item['topics'])
            # print(item['id'])
            for t in item['topics']:
                data = dict()
                data['topic_id'] = t['id']
                data['indicator_id'] = item['id']
                # print(data)
                my_cursor = my_db.cursor()
                my_cursor.execute(sql_formula, data)
                # my_db.commit()
        except Exception as e:
            print('Error: ', e)
my_cursor.close()
my_db.close()



