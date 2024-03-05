import wbdata as wb
from db.database import my_db
countries = wb.get_country()
sources = wb.get_source()
topics = wb.get_topic()

sql_formula = ('''INSERT INTO topics
                     (id,
                      value,
                      source_note)
                     VALUES ( %(id)s, %(value)s, %(source_note)s)
                  ''')

for topic in topics:
    try:
        # print(topic)
        data = dict()
        data['id'] = topic['id']
        data['value'] = topic['value']
        data['source_note'] = topic['sourceNote']
        print(data)
        my_cursor = my_db.cursor()
        my_cursor.execute(sql_formula, data)
        # my_db.commit()
    except Exception as e:
        print('Error: ', e)
my_cursor.close()
my_db.close()

