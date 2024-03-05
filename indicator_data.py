import wbdata as wb
from db.database import my_db
countries = wb.get_country()
sources = wb.get_source()
topics = wb.get_topic()
print(len(countries))

sql_formula = ('''INSERT INTO indicator_data
                     (indicator_id,
                      country_name,
                      country_iso2,
                      country_iso3,
                      date,
                      value,
                      unit,
                      obs_status,
                      decimal_val)
                     VALUES ( %(indicator_id)s, %(country_name)s, %(country_iso2)s, %(country_iso3)s, %(date)s,
                      %(value)s,%(unit)s, %(obs_status)s, %(decimal_val)s)
                  ''')
for country in countries:
    iso3code = country['id']
    print(iso3code)
    try:
        indicator_data = wb.get_data('ENF.CONT.COEN.ATDR', country=iso3code)
        for item in indicator_data:
            if item != 'None':
                print(item)
                data = dict()
                data['indicator_id'] = item['indicator']['id']
                data['country_name'] = item['country']['value']
                data['country_iso2'] = item['country']['id']
                data['country_iso3'] = item['countryiso3code']
                data['date'] = item['date']
                data['value'] = item['value']
                data['unit'] = item['unit']
                data['obs_status'] = item['obs_status']
                data['decimal_val'] = item['decimal']
                print(data)
                my_cursor = my_db.cursor()
                my_cursor.execute(sql_formula, data)
                my_db.commit()
    except Exception as e:
        print('Error: ', e)
my_cursor.close()
my_db.close()

